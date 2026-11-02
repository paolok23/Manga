"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Ejecutar migraciones automáticamente al iniciar la aplicación
try:
    call_command('migrate')
except Exception as e:
    print(f"Error al ejecutar migraciones: {e}")

application = get_wsgi_application()