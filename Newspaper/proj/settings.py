"""
Django settings for proj project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)*c823pbpw#ajiwsv_)mpu^fq@%hy(3xtcgy69ogc4m#0z1!8m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'news',
    'news.templatesargs',
    'django_filters',

    'postapps.PostConfig',
    'django.contrib.sites',
    'django_apscheduler'

# 3rd party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
# провайдеры, которые планируете использовать
    'allauth.socialaccount.providers.google',
#пользовательские приложения
    'sign',
    'protected'
]
SITE_ID = 1
DEFAULT_FROM_EMAIL = 'news@yandex.ru'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'

    
]

ROOT_URLCONF = 'proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
   # Needed to login by username in Django admin, regardless of `allauth`
   'django.contrib.auth.backends.ModelBackend',
  
   # `allauth` specific authentication methods, such as login by e-mail
   'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
#LOGIN_URL = "post/create/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'news_page/'


ACCOUNT_EMAIL_REQUIRED = True # поле email является обязательным
ACCOUNT_UNIQUE_EMAIL = True # и уникальным
ACCOUNT_USERNAME_REQUIRED = False # username теперь необязательный
ACCOUNT_AUTHENTICATION_METHOD = 'email' #аутентификация будет происходить посредством электронной почты
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' 
ACCOUNT_FORMS = {'signup': 'sign.forms.BasicSignupForm'}


APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{asctime} {levelname} {message}',
        'style': '{',  
        },
        'warning_format': {
          'format': '{asctime} {levelname} {message} {pathname}',
        'style': '{',
        },
        'error_format': {
          'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
        'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console_inf': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_warr': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_format'
        },  
        'console_err': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_format'
        },
        'file_info': {
          'level': 'INFO',
          'class': 'logging.FileHandler',
          'filename': 'general.log',
          'formatter': 'simple',
          'filters': ['require_debug_false']
        },
        'file_errors': {
          'level': 'ERROR',
          'class': 'logging.FileHandler',
          'filename': 'errors.log',
          'formatter': 'error_format',
        },
        'file_security': {
          'level': 'INFO',
          'class': 'logging.FileHandler',
          'filename': 'security.log',
        },
        'mail_admins': {
           'level': 'ERROR',
           'class': 'django.utils.log.AdminEmailHandler',
           'formatter': 'warning_format' # без стека ошибок
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console_inf', 'console_err', 'console_warr', 'file_info'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file_security'],
            'propagate': True,
            
        },
    },
}

if DEBUG:
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'