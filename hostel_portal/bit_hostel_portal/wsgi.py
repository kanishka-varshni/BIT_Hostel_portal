# bit_hostel_portal/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bit_hostel_portal.settings')

application = get_wsgi_application()
