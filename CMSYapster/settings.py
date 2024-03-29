"""
Django settings for CMSYapster project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v6k@u6in+)f$6tqe+8b!xta@_u7ra^g%@ua+!ete+2m7rrk-y%'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

BUCKET_NAME = 'yapstercms'

DB_YAPSTER = 'ye_1_db_1'

AWS_ACCESS_KEY_ID = 'AKIAILXQXCTY4QGZSFGA'

AWS_SECRET_ACCESS_KEY = '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'

# USER_GITHUB = 'chrislerus'
#
# PWD_GITHUB = '3010902213gi'
#
# CLIENT_ID_GOOGLE = '190947602394-nkskl36ugndmdhqa4tankucetlidbggt.apps.googleusercontent.com'
#
# SECRET_KEY_GOOGLE = 'rDdPo2skoreKG0bQiOM9d908'
#
# SCOPE_GOOGLE = 'https://www.googleapis.com/auth/drive'
#
# REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'psycopg2',
    'boto',
    'rest_framework',
    'oauth2client',
    'schedule',

    'tools',

    'admins',
    'announcements',
    'calendars',
    'chat',
    'cms_channels',
    'cms_search_log',
    'cms_location',
    'cms_notifications',
    'cms_reports',
    'contacts',
    'db_manager',
    'db_recover',
    'files_manager',
    #'gits',
    'groups',
    'listings',
    'stats',
    'tasks',
    'wiki',
    #
    'location',
    'manual_override',
    'notification',
    'report',
    'search',
    'stream',
    'users',
    'yap'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'CMSYapster.urls'

WSGI_APPLICATION = 'CMSYapster.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': os.path.join(BASE_DIR, 'django.sqlite3'),
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        },
     'ye_1_db_1': {
        "ENGINE": 'django.contrib.gis.db.backends.postgis',
        "HOST": "yte-1-db-1.cagmlb1zwzjw.us-east-1.rds.amazonaws.com",
        "PORT": "5432",
        "NAME": "yte_1_db_1",
        "USER": "yapster",
        "PASSWORD": "ABCD1234",
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
# https://docs.djangoproject.com/en/1.6/howto/assets-files/

STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets/'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

DATABASE_ROUTERS = ['yap.router.APIRouter']

GEOS_LIBRARY_PATH = 'C:/OSGeo4W/bin/geos_c.dll'

