# bit_hostel_portal/asgi.py

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bit_hostel_portal.settings')

application = get_asgi_application()
