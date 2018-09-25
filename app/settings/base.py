from decouple import config
 
# from dj_database_url import parse as db_url
 
from unipath import Path

# Chess board default options
BOARD_SIZE = config('BOARD_MATRIX_SIZE', default=8, cast=int)
TURNS_AMOUNT = config('TURNS_AMOUNT', default=2, cast=int)

# Project base dir
BASE_DIR = Path(__file__).ancestor(2)

DEBUG = config('DEBUG', default=False, cast=bool)

# Apps
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 
    # third party apps
    'rest_framework',
 
    # Local apps
    'backend.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Gateway and urls configs
ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database',
    }
}

# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_L10N = True
USE_TZ = False
USE_THOUSAND_SEPARATOR = True
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')

# Login Configurations
# LOGIN_URL = '/login/'
# LOGOUT_URL = '/logout/'
# LOGIN_REDIRECT_URL = ''

# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
