from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        'Eduardo',
        'rafael.hola32@gmail.com',
        'Josue1203'
    )

print("Superusuario creado")