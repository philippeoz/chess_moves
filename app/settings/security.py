from decouple import Csv, config


# Secrete key
SECRET_KEY = config('SECRET_KEY', default='69))8z7k@en(b2qey78cwa=q0)782u@duzml5c&axbhu(i&ac8')

# Host names to DEBUG=False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

# Password validators
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