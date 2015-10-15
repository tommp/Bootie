from bootie.settings import *

SECRET_KEY_DIR = '/etc/secret_key.txt'
DB_INFO_DIR = BASE_DIR + '/bootie/db_info.txt'

# SECURITY WARNING: keep the secret key used in production secret!
with open(SECRET_KEY_DIR) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Prod security settings
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}