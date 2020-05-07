"""blog URL Configuration"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("posts", views.PostViewSet)

app_name = "blog"

urlpatterns = [
    path("", include(router.urls)),
]
