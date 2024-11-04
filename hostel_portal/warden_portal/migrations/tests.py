# warden_portal/tests.py

from django.test import TestCase
from .models import Warden, LeaveRequest
from student_portal.models import Student

class WardenModelTest(TestCase):

    def setUp(self):
        student = Student.objects.create(
            name="Kanishka", email="kanishka@example.com", 
            address="Coimbatore", hostel_name="Hostel A", 
            room_number="101", floor_number=1, 
            contact_details="9876543210"
        )
        self.warden = Warden.objects.create(name="Warden A", email="warden@example.com")
        LeaveRequest.objects.create(student=student, leave_type="Regular", 
                                     from_date="2024-10-20", to_date="2024-10-25", 
                                     reason="Family function")

    def test_warden_name(self):
        warden = Warden.objects.get(email="warden@example.com")
        self.assertEqual(warden.name, "Warden A")
