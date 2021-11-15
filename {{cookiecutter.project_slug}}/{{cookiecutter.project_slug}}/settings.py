import os

from unipath import Path
from decouple import config, Csv
from dj_database_url import parse as dburl

{%- if cookiecutter.use_database_schema == "y" %}
import sys
{% endif %}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = Path(__file__).ancestor(3)
APPS_DIR = ROOT_DIR.child('{{ cookiecutter.project_slug }}')

SECRET_KEY = config('SECRET_KEY', default=('0' * 50))
DEBUG = config('DEBUG', default=False, cast=bool)
SENTRY_DSN = config("SENTRY_DSN", default=None)

{%- if cookiecutter.use_database_schema == "y" %}
USE_SCHEMA = config('USE_SCHEMA', default=False, cast=bool)
{% endif %}
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_extensions',
    'corsheaders',
    'drf_yasg',
    'django_filters',
    {%- if cookiecutter.use_graphql == "y" %}
    'graphene_django',
    {% endif %}
]

LOCAL_APPS = [
    'core',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{ cookiecutter.project_slug }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]

WSGI_APPLICATION = '{{ cookiecutter.project_slug }}.wsgi.application'

# Sentry
RAVEN_CONFIG = {"dsn": SENTRY_DSN}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=DATABASE_URL, cast=dburl)
}
{%- if cookiecutter.use_database_schema == "y" %}
if 'test' in sys.argv:
    DATABASES['OPTIONS'] = {
        'options': '-c search_path={{ cookiecutter.project_slug }}'
    }
elif USE_SCHEMA:
    DATABASES['default']['OPTIONS'] = {
        'options': '-c search_path={{ cookiecutter.project_slug }}'
    }
{% endif %}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'  # noqa: E501
    },
]

LOGGING = {
    'version': 1,
    'formatters': {
        'console': {'format': '[%(asctime)s][%(levelname)s]-%(message)s'},
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
            '%(process)d %(thread)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'}
    },
}
if DEBUG:  # For dev environment
    LOGGING['disable_existing_loggers'] = False
    LOGGING['handlers'] = {
        'console': {'class': 'logging.StreamHandler', 'formatter': 'console'},
    }
    LOGGING['loggers'] = {
        '': {'level': 'INFO', 'handlers': ['console']},
        'django.db': {'level': 'DEBUG', 'handlers': ['console']},
    }
else:
    LOGGING['handlers'] = {}
    LOGGING['loggers'] = {}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = '{{ cookiecutter.timezone }}'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')

# CORS configs
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'authentication',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# Rest Framework
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'COERCE_DECIMAL_TO_STRING': False,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination'
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

# Send mail configurations
# For development, use Mailcatcher: https://mailcatcher.me/
EMAIL_BACKEND = config(
    'EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend'
)
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=25)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default=None)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default=None)

# Admin user settings
ADMIN_USERNAME = config("ADMIN_USERNAME", default="admin")
ADMIN_PASSWORD = config("ADMIN_PASSWORD", default="admin")
ADMIN_TOKEN = config("ADMIN_TOKEN", default=None)

{%- if cookiecutter.use_graphql == "y" %}
# Graphene settings
GRAPHENE = {
    'SCHEMA': 'core.schema.schema',
}

{% endif %}
