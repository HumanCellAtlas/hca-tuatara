# -*- coding: utf-8 -*-
from .base import *

DEBUG = False
 
ALLOWED_HOSTS = ["tuatara.data.humancellatlas.org", "tuatara.gi.ucsc.edu", "hgwdev.gi.ucsc.edu", "3.15.142.222", "127.0.0.1", "172.31.12.176"]

# Settings to better secure the cookies from security exploits
# since we are serving production deployment over https
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

STATIC_ROOT="/home/tuatara/static"

SECRET_KEY = os.environ["HCAT_SECRET_KEY"]

#INSTALLED_APPS += [
#    'mod_wsgi.server',
#]

