"""
WSGI config for motorqtask project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from motorqtask.tasks import scheduler 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'motorqtask.settings')

application = get_wsgi_application()


#running the scheduler
# try:
#     from apscheduler.schedulers.background import BackgroundScheduler
#     scheduler.start()
# except ImportError:
#     pass
