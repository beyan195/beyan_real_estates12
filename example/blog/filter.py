from django_filters import rest_framework as filters

from .models import Post


class PostFilter(filters.FilterSet):

    created_at = filters.DateFromToRangeFilter("created_at")

    class Meta:
        model = Post
        fields = (
            "type",
            "is_open",
            "views",
            "created_at",
        )
