# warden_portal/views.py

from django.shortcuts import render
from .models import LeaveRequest, RoomBooking
from student_portal.models import Student

def dashboard(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'warden/dashboard.html', {'leave_requests': leave_requests})

def leave_approval(request):
    if request.method == 'POST':
        # Logic to handle leave approval/rejection
        pass
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'warden/leave_approval.html', {'leave_requests': leave_requests})

def room_details(request):
    # Logic to show room details
    return render(request, 'warden/room_details.html')

def room_booking(request):
    if request.method == 'POST':
        # Logic to handle room booking verification
        pass
    room_bookings = RoomBooking.objects.all()
    return render(request, 'warden/room_booking.html', {'room_bookings': room_bookings})
