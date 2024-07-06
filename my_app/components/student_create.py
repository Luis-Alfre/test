from django_unicorn.components import UnicornView
from my_app.models import Student


class StudentCreateView(UnicornView):
    student_name = ''
    student_age = ''
    student_email = ''
    student_note_1 = ''
    student_note_2 = ''
    student_note_3 = ''

    def create_student(self):
        student = Student(
            name=self.student_name,
            age=self.student_age,
            email=self.student_email,
            note_1=self.student_note_1,
            note_2=self.student_note_2,
            note_3=self.student_note_3,
        )
        student.save()
