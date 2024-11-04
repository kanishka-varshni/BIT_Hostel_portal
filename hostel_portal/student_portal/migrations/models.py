# student_portal/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    hostel_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    floor_number = models.IntegerField()
    contact_details = models.CharField(max_length=15)

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


class Room(models.Model):
    hostel_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    floor_number = models.IntegerField()
    total_cots = models.IntegerField()
    occupied_cots = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.hostel_name} - {self.room_number}"
