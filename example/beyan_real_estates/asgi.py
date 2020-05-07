"""
ASGI config for beyan_real_estates project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beyan_real_estates.settings")

application = get_asgi_application()
