# warden_portal/models.py

from django.db import models
from student_portal.models import Student

class Warden(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class LeaveRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.student.name} - {self.status}"


class RoomBooking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hostel_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    booking_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.student.name} - {self.hostel_name} {self.room_number} ({self.status})"
