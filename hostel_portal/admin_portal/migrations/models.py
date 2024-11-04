# admin_portal/models.py

from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Hostel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    floor_number = models.IntegerField()
    
    def __str__(self):
        return self.name

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Feedback from {self.student.name}: {self.status}"

class RoomBooking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.student.name} - Room {self.room_number} ({self.status})"
