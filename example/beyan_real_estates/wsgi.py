"""
WSGI config for beyan_real_estates project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beyan_real_estates.settings")

application = get_wsgi_application()
