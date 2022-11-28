from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/root/MyLife/mylife/static',
]

ADMINS = MANAGERS = (
    ('jay', 'leafleaving@gmail.com'),
)

# EMAIL_HOST = '<email smtp server address>'
# EMAIL_HOST_USER = '<login username>'
# EMAIL_HOST_PASSWORD = '<PASSWORD>'
# EMAIL_SUBJECT_PREFIX = '邮箱标题前缀'
# DEFAULT_FROM_EMAIL = '展示发件人的地址'
# SERVER_EMAIL = '<邮件服务器>'

# STATIC_ROOT = '/root/...'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                    '%(funcName)s: %(lineno)d %(message)s'
        },
    },
    
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/tmp/logs/typeidea.log',
            'formatter': 'default',
            'maxBytes': 1024*1024, #1M
            'backupCount': 5,
        },
    },
    
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}