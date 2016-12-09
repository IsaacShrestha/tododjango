from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework.authentication import *
from rest_framework.decorators import *

from models import TodoItem
from serializers import TodoItemSerializer
from forms import RegistrationForm
from models import *
from permissions import BelongsToUser
import json

class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TodoItems to be CRUDed.
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, BelongsToUser,)

    def get_queryset(self):
	    return TodoItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
	    serializer.save(user=user.request.user)

@require_http_methods(["POST"])
@csrf_exempt
def register(request):
    """
    API endpoint to register a new user.
    """
    try:
        payload = json.loads(request.body)
    except ValueError:
        return JsonResponse({"error": "Unable to parse request body"}, status=400)

    form = RegistrationForm(payload)

    if form.is_valid():
        user = User.objects.create_user(form.cleaned_data["username"],
                                        form.cleaned_data["email"],
                                        form.cleaned_data["password"])
        print user
        user.save()

        return JsonResponse({"success": "User registered."}, status=201)

    return HttpResponse(form.errors.as_json(), status=400, content_type="application/json")