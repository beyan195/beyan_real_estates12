from typing import Dict, Tuple

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, permissions, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response

from . import models, serializers
from .filter import PostFilter


class PostViewSet(viewsets.ModelViewSet):

    queryset = models.Post.objects.filter(is_open=True)

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    filterset_class = PostFilter

    search_fields = ("title", "description")

    ordering = ("-created_at",)

    ordering_fields = ("title", "created_at")

    lookup_field = "unique_id"

    def get_serializer_class(self, *args: Tuple, **kwargs: Dict):

        if self.action == "retrieve":
            return serializers.PostSerializer

        return serializers.PostListSerializer

    def get_permissions(self):

        if self.action == "create":

            permission_classes = (permissions.IsAuthenticated,)

        elif self.action == "update" or self.action == "partial_update":

            permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

        elif self.action == "destroy":

            permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

        else:

            permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        return [permission() for permission in permission_classes]

    def retrieve(self, request: Request, *args, **kwargs):
        try:

            post = models.Post.objects.get(is_open=True, unique_id=kwargs.get("unique_id"))

            post.views += 1

            post.save()

            serializer = self.get_serializer(post)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as error:
            raise exceptions.ValidationError(
                detail={"detail": "Not Found"}, code="not found"
            )
