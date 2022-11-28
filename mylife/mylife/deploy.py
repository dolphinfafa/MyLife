"""
WSGI config for tombstone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#orginal os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tombstone.settings")
profile = os.environ.get('MYLIFE_PROFILE', 'product')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mylife.settings.%s" % profile)

application = get_wsgi_application()