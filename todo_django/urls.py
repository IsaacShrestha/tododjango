from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from todo.views import TodoItemViewSet, register
from rest_framework.authtoken.views import obtain_auth_token




router = routers.DefaultRouter(trailing_slash=False)
router.register("todos", TodoItemViewSet)

urlpatterns = [
	url(r'^api-auth-token/', obtain_auth_token),
    url(r'^api/', include(router.urls)),
    url(r'^api-register/', register),
]



