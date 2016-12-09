from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from todo.views import TodoItemViewSet, register




router = routers.DefaultRouter(trailing_slash=False)
router.register("todos", TodoItemViewSet, base_name="todo")

urlpatterns = [
	url(r'^api-auth-token/', obtain_auth_token),
    url(r'^api/', include(router.urls)),
    url(r'^api-register/', register),
    url(r'^admin/', admin.site.urls),
]



