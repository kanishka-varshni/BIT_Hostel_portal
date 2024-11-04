# student_portal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='student_dashboard'),
    path('leave_apply/', views.leave_apply, name='leave_apply'),
    path('room_details/', views.room_details, name='room_details'),
    path('room_vacancy/', views.room_vacancy, name='room_vacancy'),
    path('info_access/', views.info_access, name='info_access'),
    path('feedback/', views.feedback, name='feedback'),
]
