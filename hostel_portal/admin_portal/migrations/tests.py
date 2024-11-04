# admin_portal/tests.py

from django.test import TestCase
from .models import Admin, Hostel, Student

class AdminModelTest(TestCase):

    def setUp(self):
        self.admin = Admin.objects.create(name="Admin A", email="admin@example.com")
        self.hostel = Hostel.objects.create(name="Hostel A", address="Coimbatore")
        self.student = Student.objects.create(
            name="Kanishka", email="kanishka@example.com",
            address="Coimbatore", hostel=self.hostel,
            room_number="101", floor_number=1
        )

    def test_admin_name(self):
        admin = Admin.objects.get(email="admin@example.com")
        self.assertEqual(admin.name, "Admin A")

    def test_student_hostel(self):
        student = Student.objects.get(email="kanishka@example.com")
        self.assertEqual(student.hostel.name, "Hostel A")
