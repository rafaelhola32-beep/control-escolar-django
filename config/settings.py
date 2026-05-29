
import os
import dj_database_url
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kk8pvj_hv9r8x7=b+1pe6l0dxx&4n49#+!^(z%w_$(pisok9&6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'control-escolar-2026.onrender.com',
    '127.0.0.1',
    'localhost'
]

CSRF_TRUSTED_ORIGINS = [
    'https://control-escolar-2026.onrender.com'
]


# Application definition

INSTALLED_APPS = [
    
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_extensions',
    'django.contrib.staticfiles',

    'carreras',
    'profesores',
    'estudiantes',
    'materias',
    'aulas',
    'horarios',
    'grupos',
    'calificaciones',
    'periodos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases




DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    DATABASE_URL = str(DATABASE_URL)

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

JAZZMIN_SETTINGS = {

    # TITULOS
    "site_title": "Control Escolar",

    "site_header": "Sistema Control Escolar",

    "site_brand": "Control Escolar",

    "welcome_sign": "Bienvenido Administrador",

    "copyright": "Control Escolar 2026",

    # LOGO
    "site_logo_classes": "img-circle",

    # BUSCADOR
    "search_model": "auth.User",

    # MENU SUPERIOR
    "topmenu_links": [

        {
            "name": "Inicio",
            "url": "admin:index",
            "permissions": ["auth.view_user"]
        },

    ],

    # SIDEBAR
    "show_sidebar": True,

    "navigation_expanded": True,

    # ORDEN DE APPS
    "order_with_respect_to": [

        "estudiantes",
        "profesores",
        "materias",
        "grupos",
        "calificaciones",

    ],

    # ICONOS
    "icons": {

        "auth": "fas fa-users-cog",

        "auth.user": "fas fa-user",

        "auth.Group": "fas fa-users",

        "estudiantes.estudiante": "fas fa-user-graduate",

        "profesores.profesor": "fas fa-chalkboard-teacher",

        "materias.materia": "fas fa-book",

        "grupos.grupo": "fas fa-users",

        "calificaciones.calificacion": "fas fa-star",

    },

    # ICONOS POR DEFECTO
    "default_icon_parents": "fas fa-chevron-circle-right",

    "default_icon_children": "fas fa-circle",

    # MODALES
    "related_modal_active": True,

    # UI BUILDER
    "show_ui_builder": True,

}

JAZZMIN_UI_TWEAKS = {

    "theme": "darkly",

    "dark_mode_theme": "darkly",

    "navbar": "navbar-primary navbar-dark",

    "no_navbar_border": True,

    "accent": "accent-primary",

    "navbar_small_text": False,

    "sidebar": "sidebar-dark-primary",

    "sidebar_nav_small_text": False,

    "sidebar_disable_expand": False,

    "sidebar_nav_child_indent": True,

    "sidebar_nav_compact_style": False,

    "sidebar_nav_legacy_style": False,

    "sidebar_nav_flat_style": False,

    "theme_colour": "primary",

    "button_classes": {

        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"

    }

}
import os
import django

if os.environ.get('CREATE_ADMIN') == 'true':
    django.setup()

    from django.contrib.auth.models import User

    if not User.objects.filter(username='Eduardo').exists():
        User.objects.create_superuser(
            'Eduardo',
            'correo@correo.com',
            'Josue1203'
        )
