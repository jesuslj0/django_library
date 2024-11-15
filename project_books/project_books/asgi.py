"""
ASGI config for project_books project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_books.settings')
sys.path.append(os.path.join(os.path.dirname(__file__), 'project_books'))

application = get_asgi_application()
