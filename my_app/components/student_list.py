from django_unicorn.components import UnicornView
from my_app.models import Student
from django.db.models import Avg

class StudentListView(UnicornView):
    students = []
    search_term = ''
    editing_student_id = None
    editing_student = None
    editing_student_name = ''
    editing_student_age = ''
    editing_student_email = ''
    editing_student_note_1 = ''
    editing_student_note_2 = ''
    editing_student_note_3 = ''
    avg_age = 0
    avg_note_1 = 0
    avg_note_2 = 0
    avg_note_3 = 0


    def mount(self):
        self.load_students()

    def load_students(self):
        self.students = list(Student.objects.all())
        self.calculate_avg()

    def search_students(self):
        if self.search_term:
            self.students = list(Student.objects.filter(name__icontains=self.search_term) | Student.objects.filter(email__icontains=self.search_term))
        else:
            self.load_students()

    def start_editing_student(self, student_id):
        self.editing_student = 1
        student = Student.objects.get(id=student_id)
        self.editing_student_id = student.id
        self.editing_student_name = student.name
        self.editing_student_age = student.age
        self.editing_student_email = student.email
        self.editing_student_note_1 = student.note_1
        self.editing_student_note_2 = student.note_2
        self.editing_student_note_3 = student.note_3

    def cancel_editing_student(self):
        self.editing_student = None
        self.load_students()

    def save_student_changes(self):
        student = Student.objects.get(id=self.editing_student_id)
        student.name = self.editing_student_name
        student.age = self.editing_student_age
        student.email = self.editing_student_email
        student.note_1 = self.editing_student_note_1
        student.note_2 = self.editing_student_note_2
        student.note_3 = self.editing_student_note_3

        student.save()
        self.cancel_editing_student()
        self.load_students()

    def calculate_avg(self):
        self.avg_age = Student.objects.aggregate(avg_age=Avg('age'))['avg_age'] or 0
        self.avg_note_1 = Student.objects.aggregate(avg_note_1=Avg('note_1'))['avg_note_1'] or 0
        self.avg_note_2 = Student.objects.aggregate(avg_note_2=Avg('note_2'))['avg_note_2'] or 0
        self.avg_note_3 = Student.objects.aggregate(avg_note_3=Avg('note_3'))['avg_note_3'] or 0

        
