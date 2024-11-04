# warden_portal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='warden_dashboard'),
    path('leave_approval/', views.leave_approval, name='leave_approval'),
    path('room_details/', views.room_details, name='warden_room_details'),
    path('room_booking/', views.room_booking, name='room_booking'),
]
