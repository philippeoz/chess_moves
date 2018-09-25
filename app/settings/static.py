from decouple import config
 
from .base import BASE_DIR, DEBUG
 
 
# Static files url
STATIC_URL = config('STATIC_URL', default='/static/')
STATIC_ROOT = BASE_DIR.child('frontend', 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR.child('frontend', 'static'),
]
 
# File finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
 
# Template backends, processors and finders
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # BASE_DIR.child('frontend', 'templates'),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]