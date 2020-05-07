from django.contrib import admin

from .models import Post, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = (
        "title",
        "type",
        "is_open",
        "views",
        "created_at",
    )

    list_filter = ["type", "is_open", "views", "created_at"]
    search_fields = ["title", "description"]
    readonly_fields = ("unique_id", "views")


admin.site.register(Post, PostAdmin)
admin.site.register(Image)
