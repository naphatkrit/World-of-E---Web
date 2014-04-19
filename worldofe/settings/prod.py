from common import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME': 'worldofe_db',
        'USER': 'worldofe_admin',
        'PASSWORD': '#Ps12Ei34'
    }
}

SECRET_KEY = 'lkjsd@#REAFWsdfija$^WTAREGFDZL#QJ$5wreaFTWJ$%LK&^U&JRTYR'
