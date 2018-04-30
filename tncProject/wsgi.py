"""
WSGI config for tncProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

# from dj_static import Cling
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tncProject.settings")

# application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(get_wsgi_application())
