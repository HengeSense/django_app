import sys
import os

#Insert the root django app directory into the python path
sys.path.insert(0,os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)) ,'..')))

import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_app.settings'

application = django.core.handlers.wsgi.WSGIHandler()
