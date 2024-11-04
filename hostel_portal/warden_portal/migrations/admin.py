# warden_portal/admin.py

from django.contrib import admin
from .models import Warden, LeaveRequest, RoomBooking

# Register your models here.
admin.site.register(Warden)
admin.site.register(LeaveRequest)
admin.site.register(RoomBooking)
