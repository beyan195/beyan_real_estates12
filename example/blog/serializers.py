from rest_framework import serializers

from .models import Image, Post


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField(read_only=True)


class PostListSerializer(serializers.Serializer):

    unique_id = serializers.UUIDField(read_only=True)

    title = serializers.CharField(read_only=True)

    type = serializers.CharField(read_only=True)

    views = serializers.IntegerField(read_only=True)

    is_open = serializers.BooleanField(read_only=True)

    created_at = serializers.DateTimeField(read_only=True)

    cover = serializers.ImageField(read_only=True)


class PostSerializer(serializers.Serializer):

    unique_id = serializers.UUIDField(read_only=True)

    title = serializers.CharField(read_only=True)

    description = serializers.CharField(read_only=True)

    type = serializers.CharField(read_only=True)

    views = serializers.IntegerField(read_only=True)

    is_open = serializers.BooleanField(read_only=True)

    created_at = serializers.DateTimeField(read_only=True)

    cover = serializers.ImageField(read_only=True)

    list_of_images = ImageSerializer(many=True)
