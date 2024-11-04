# admin_portal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('hostel_management/', views.hostel_management, name='hostel_management'),
    path('biometric_attendance/', views.biometric_attendance, name='biometric_attendance'),
    path('room_bookings/', views.room_bookings, name='room_bookings'),
    path('student_communication/', views.student_communication, name='student_communication'),
    path('leave_management/', views.leave_management, name='leave_management'),
    path('room_management/', views.room_management, name='room_management'),
    path('outsider_bookings/', views.outsider_bookings, name='outsider_bookings'),
    path('group_communication/', views.group_communication, name='group_communication'),
    path('student_management/', views.student_management, name='student_management'),
    path('feedback_management/', views.feedback_management, name='feedback_management'),
]
