import os
import sys

sys.path.append('/home/honestemu/public/emilabraham.com/personalpage')

os.environ['PYTHON_EGG_CACHE'] = '/home/honestemu/public/emilabraham.com/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'personalpage.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
