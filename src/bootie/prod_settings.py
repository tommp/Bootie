"""
Django prod_settings for bootie project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

GIT_ROOT = os.path.abspath(__file__).rsplit(os.path.sep, 3)[0]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__) 
DB_INFO_DIR = BASE_DIR + '/bootie/db_info.txt'
SECRET_KEY_DIR = '/etc/secret_key.txt'

# Prod security settings
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

with open(SECRET_KEY_DIR) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = (
    ('Tom Meland Pedersen', 'tompersen@gmail.com')
)

MANAGERS = ADMINS

ALLOWED_HOSTS = [
    '127.0.0.1',
    'www.ntnuipadling.no',
    'ntnuipadling.no',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Secondary apps
    'imagekit',
    'static_precompiler',
    'captcha',
    #Bootie apps
    'posts',
    'index',
    'weatherforecast',
    'info',
    'paddleusers',
    'events',
    'galleries',
    'ads'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'bootie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'bootie/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'index.context_processors.base_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'bootie.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

with open(DB_INFO_DIR) as f:
    content = [x.strip('\n') for x in f.readlines()]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': content[0],
        'USER': content[1],
        'PASSWORD': content[2],
        'HOST': content[3],
        'PORT': '',

    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_DIR, 'public', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'static'),
)

#######################
#    Uploded media    #
#######################

#Media files, images, videos etc.
MEDIA_ROOT = os.path.join(GIT_ROOT, 'public', 'media')
MEDIA_URL = '/media/'



#######################
#     Login info      #
#######################

LOGIN_URL = 'bootie_login'
LOGOUT_URL = 'bootie_logout'
LOGIN_REDIRECT_URL = '/'



#######################
#       Captcha       #
#######################

#######################
#   Easy thumbnails   #
#######################

THUMBNAIL_BASEDIR = 'thumbs'
THUMBNAIL_DEBUG = False
