from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
