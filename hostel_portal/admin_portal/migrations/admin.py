# admin_portal/admin.py

from django.contrib import admin
from .models import Admin, Hostel, Student, Feedback, RoomBooking

# Register your models here.
admin.site.register(Admin)
admin.site.register(Hostel)
admin.site.register(Student)
admin.site.register(Feedback)
admin.site.register(RoomBooking)
