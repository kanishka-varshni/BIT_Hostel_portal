# student_portal/tests.py

from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):

    def setUp(self):
        Student.objects.create(name="Kanishka", email="kanishka@example.com", 
                                address="Coimbatore", hostel_name="Hostel A", 
                                room_number="101", floor_number=1, 
                                contact_details="9876543210")

    def test_student_name(self):
        student = Student.objects.get(email="kanishka@example.com")
        self.assertEqual(student.name, "Kanishka")
