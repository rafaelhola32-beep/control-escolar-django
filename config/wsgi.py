import os

if os.environ.get('CREATE_SUPERUSER') == 'true':
    import django
    django.setup()

    from django.contrib.auth.models import User

    if not User.objects.filter(username='Eduardo').exists():
        User.objects.create_superuser(
            'Eduardo',
            'rafael.hola32@gmail.com',
            'Josue1203'
        )

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
