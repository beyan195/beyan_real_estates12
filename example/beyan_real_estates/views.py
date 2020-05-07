from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import secrets

from blog.models import Post


def home(request):
    posts = Post.objects.filter(is_open=True)
    posts_slider = []
    for _ in range(3):
        posts_slider.append(secrets.choice(posts))
    return render(request=request, template_name="home.html", context={"posts": posts[:6], "posts_slider": set(posts_slider)})


def list_property(request):
    posts = Post.objects.filter(is_open=True)
    return render(request=request, template_name="property.html", context={"posts": posts})


def property_detail(request, unique_id):
    post = get_object_or_404(Post, unique_id=unique_id)
    return render(request=request, template_name="property_detail.html", context={"post": post})


@api_view(["POST"])
def login(request: Request) -> Response:

    user = authenticate(username=request.data.get("username"), password=request.data.get("password"), request=request)

    if user:
        return Response({"detail": f"{request.headers.get('Host')}/unk/"}, status=status.HTTP_200_OK)

    return Response({"detail": "Incorrect"}, status=status.HTTP_400_BAD_REQUEST)
