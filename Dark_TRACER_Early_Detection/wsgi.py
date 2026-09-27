"""
WSGI config for Dark_TRACER_Early_Detection project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'Dark_TRACER_Early_Detection.settings'
)

application = get_wsgi_application()