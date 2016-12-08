from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from todo.views import TodoItemViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register("todos", TodoItemViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]



