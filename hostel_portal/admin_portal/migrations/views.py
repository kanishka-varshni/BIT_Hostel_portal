# admin_portal/views.py

from django.shortcuts import render
from .models import Feedback, RoomBooking, Student

def dashboard(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'admin/dashboard.html', {'feedbacks': feedbacks})

def hostel_management(request):
    # Logic to manage hostels
    return render(request, 'admin/hostel_management.html')

def biometric_attendance(request):
    # Logic to show biometric attendance
    return render(request, 'admin/biometric_attendance.html')

def room_bookings(request):
    room_bookings = RoomBooking.objects.all()
    return render(request, 'admin/room_bookings.html', {'room_bookings': room_bookings})

def student_communication(request):
    # Logic for student communication
    return render(request, 'admin/student_communication.html')

def leave_management(request):
    # Logic for leave management
    return render(request, 'admin/leave_management.html')

def room_management(request):
    # Logic for room management
    return render(request, 'admin/room_management.html')

def outsider_bookings(request):
    # Logic for outsider bookings
    return render(request, 'admin/outsider_bookings.html')

def group_communication(request):
    # Logic for group communication
    return render(request, 'admin/group_communication.html')

def student_management(request):
    students = Student.objects.all()
    return render(request, 'admin/student_management.html', {'students': students})

def feedback_management(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'admin/feedback_management.html', {'feedbacks': feedbacks})
