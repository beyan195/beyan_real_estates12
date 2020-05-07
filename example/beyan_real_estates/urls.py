"""
beyan_real_estates URL Configuration
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from .views import login, home, list_property, property_detail

urlpatterns = i18n_patterns(
    path("", home, name="home"),
    path("properties/", list_property, name="list_property"),
    path("unk/", admin.site.urls),
    path("api/login/", login),
    path("api/blog/", include("blog.urls")),
    path(
        ".well-known/security.txt",
        TemplateView.as_view(template_name="security.txt", content_type="text/plain",),
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain",),
    ),
    path("<uuid:unique_id>/", property_detail, name="property_detail"),

    prefix_default_language=False,
)

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))] + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
