from django.test import TestCase

from my_app.models import Student
from django.urls import reverse

class StudentModelTest(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(
            name="John Doe",
            age=20,
            email="john@example.com",
            note_1=85,
            note_2=90,
            note_3=88
        )
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.email, "john@example.com")

    def setUp(self):
        self.student = Student.objects.create(
            name="John Doe",
            age=20,
            email="john@example.com",
            note_1=85,
            note_2=90,
            note_3=88
        )

    def test_student_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.student.name)