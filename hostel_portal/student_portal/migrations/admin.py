# student_portal/admin.py

from django.contrib import admin
from .models import Student, LeaveRequest, Room

# Register your models here.
admin.site.register(Student)
admin.site.register(LeaveRequest)
admin.site.register(Room)
