import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


def posts_upload_to(instance: "Image", filename: str):

    return f"images/posts/{instance.post.title}/{filename}"


def post_upload_to(instance: "Post", filename: str):

    return f"images/posts/cover/{instance.title}/{filename}"


class Type(models.TextChoices):

    House = ("House", _("House"))

    Car = ("Car", _("Car"))


class Post(models.Model):

    unique_id = models.UUIDField(
        verbose_name=_("unique_id"), editable=False, unique=True, default=uuid.uuid4
    )

    title = models.CharField(verbose_name=_("title"), max_length=300)

    description = models.TextField(verbose_name=_("description"))

    cover = models.ImageField(
        upload_to=post_upload_to, verbose_name=_("cover"), blank=True, null=True,
    )

    type = models.CharField(
        verbose_name=_("type"), choices=Type.choices, default=Type.House, max_length=10
    )

    is_open = models.BooleanField(verbose_name=_("is open"), default=True)

    views = models.PositiveIntegerField(
        verbose_name=_("views"), default=0, editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def list_of_images(self):
        return self.images.all()


class Image(models.Model):

    image = models.ImageField(upload_to=posts_upload_to, verbose_name=_("image"))

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_("post"),
        related_name="images",
        db_index=True,
    )

    def __str__(self):
        return f"{self.image.url}"

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
