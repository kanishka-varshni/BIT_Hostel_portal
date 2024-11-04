# student_portal/views.py

from django.shortcuts import render
from .models import Student, LeaveRequest, Room

def dashboard(request):
    # Fetch student information
    student = Student.objects.first()  # Replace with actual logic to get logged-in student
    return render(request, 'student/dashboard.html', {'student': student})

def leave_apply(request):
    if request.method == 'POST':
        # Logic to handle leave application submission
        pass
    return render(request, 'student/leave_apply.html')

def room_details(request):
    student = Student.objects.first()  # Replace with actual logic
    return render(request, 'student/room_details.html', {'student': student})

def room_vacancy(request):
    rooms = Room.objects.all()  # Logic to filter rooms based on criteria
    return render(request, 'student/room_vacancy.html', {'rooms': rooms})

def info_access(request):
    # Logic to access information
    return render(request, 'student/info_access.html')

def feedback(request):
    if request.method == 'POST':
        # Logic to handle feedback submission
        pass
    return render(request, 'student/feedback.html')
