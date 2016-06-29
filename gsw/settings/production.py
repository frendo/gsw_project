# -*- coding: utf-8 -*-
from .base import *
DEBUG = False
psycopg2==2.6.1
python-social-auth==0.2.19
six==1.10.0
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

