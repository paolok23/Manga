import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Si estamos en Vercel, ejecutamos las migraciones automáticamente en la base de datos temporal
if os.environ.get('VERCEL'):
    try:
        call_command('migrate')
    except Exception as e:
        print(f"Error al ejecutar migraciones automáticas: {e}")

application = get_wsgi_application()