# bit_hostel_portal/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student_portal.urls')),
    path('warden/', include('warden_portal.urls')),
    path('admin_portal/', include('admin_portal.urls')),
]
