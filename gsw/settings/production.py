# -*- coding: utf-8 -*-
from .base import *
DEBUG = False
DATABASES = { 
         'default': {
                     'ENGINE': 'django.db.backends.postgresql_psycopg2',
                     'NAME': get_env_variable('DATABASE_NAME'),
                     'USER': get_env_variable('DATABASE_USER'),
                     'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
                     'HOST': 'frendo-165.postgres.pythonanywhere-services.com',
                     'PORT': '10165',                                                                                                                                                                         
                 }   
 }
 
FIXTURE_DIRS = ( 
    os.path.join(BASE_DIR, 'fixtures'),
)

