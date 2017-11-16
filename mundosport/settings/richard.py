from .base import *
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if DEBUG:
    # DJANGO DEBUG TOOLBAR
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        INSTALLED_APPS += ('debug_toolbar', )
        MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

    try:
        import django_extensions
    except ImportError:
        pass
    else:
        INSTALLED_APPS += ('django_extensions', )


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      }
}

INTERNAL_IPS = ('127.0.0.1',)


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT='/opt/statics/mundosport/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

#STATICFILES_DIRS = (
#os.path.join(BASE_DIR, 'mundosport', 'static'),
#)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

ALLOWED_HOSTS = ['*']
