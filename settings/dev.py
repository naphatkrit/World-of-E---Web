from common import *

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# ########## END DEBUG CONFIGURATION

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'worldofe_db',
        'USER': 'worldofe_admin',
        'PASSWORD': '#Ps12Ei34'
    }
}
########## END DATABASE CONFIGURATION

SECRET_KEY = 'aflkdjasldkfjka;weru2p0384ijorn;kamwE@Q#RWDFSZQ@#RwefAEWJ#REF'

