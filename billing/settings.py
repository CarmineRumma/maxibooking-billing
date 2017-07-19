"""
Django settings for billing project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Local settings
try:
    from .local_settings import *
except ImportError:
    pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition
INSTALLED_APPS = [
    'adminactions',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'debug_toolbar',
    'django_extensions',
    'reversion',
    'rainbowtests',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'rest_framework',
    'rest_framework.authtoken',
    'rosetta',
    'ordered_model',
    'cities_light',
    'django_filters',

    # mb apps
    'billing',
    'clients',
    'hotels',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'billing.middleware.WhodidMiddleware',
]

ROOT_URLCONF = 'billing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'billing/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'billing.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.\
UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (('ru', 'Russian'), ('en', 'English'), )

TIME_ZONE = 'Europe/Dublin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

INTERNAL_IPS = ['127.0.0.1']

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'billing/static'),
                    os.path.join(BASE_DIR, 'node_modules'), )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', )

FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'), )
LOCALE_PATHS = (os.path.join(os.path.dirname(__file__), "locale"),
                os.path.join(os.path.dirname(__file__), "app_locale"), )

EMAIL_SUBJECT_PREFIX = '[maxi-booking.com]: '

# Two factor auth
LOGIN_URL = 'two_factor:login'
LOGOUT_URL = "admin:logout"
LOGIN_REDIRECT_URL = 'admin:index'

# Celery
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Dublin'
CELERY_ALWAYS_EAGER = False

# Django phonenumber
PHONENUMBER_DB_FORMAT = 'INTERNATIONAL'

# Tests
TEST_RUNNER = 'rainbowtests.test.runner.RainbowDiscoverRunner'

# Django restframework
REST_FRAMEWORK = {
    'DEFAULT_VERSION':
    '1.0',
    'DEFAULT_VERSIONING_CLASS':
    'rest_framework.versioning.AcceptHeaderVersioning',
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':
    100,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_FILTER_BACKENDS':
    ('django_filters.rest_framework.DjangoFilterBackend',
     'rest_framework.filters.SearchFilter',
     'rest_framework.filters.OrderingFilter', ),
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework.authentication.TokenAuthentication',
     'rest_framework.authentication.SessionAuthentication', )
}

# Cities light
CITIES_LIGHT_TRANSLATION_LANGUAGES = ['en', 'ru']
CITIES_LIGHT_APP_NAME = 'hotels'
