"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*j%%41e=!1y0hd7ev%)tkjt1&3pb!ov6r%u4gdk!oicvoo%%9!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
    'json_field',
    'data',
    'djangobower',
	'django_nvd3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



MEDIA_ROOT = os.path.join(BASE_DIR, '../mysite/mysite/static')

BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../mysite/mysite/static'),
	os.path.join(BASE_DIR, '../mysite/components/bower_components/'),

	)

staticfiles_finders = (
    'django.contrib.staticfiles.finders.filesystemfinder',
    'django.contrib.staticfiles.finders.appdirectoriesfinder',
    'djangobower.finders.bowerfinder',
)


#Directories for templates

TEMPLATE_DIRS = (
    #os.path.join(BASE_DIR, '../mysite/mysite/template'),
	os.path.join(BASE_DIR, '../mysite/template'),
)

#BOWER_PATH = '/usr/local/bin/bower'

BOWER_INSTALLED_APPS = (
    'd3#3.3.6',
    'nvd3#1.1.12-beta',
)
