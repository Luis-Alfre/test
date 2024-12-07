import time
from django.test import TestCase
from my_app.models import Student
from django.urls import reverse
from my_app.components.student_list import StudentListView
from my_app.components.student_create import StudentCreateView

class StudentModelTest(TestCase):
    def setUp(self):
        return

    # Seguridad
    def test_age_not_number(self):
        # Intentar inyectar código JavaScript
        component = StudentCreateView(component_name='student_create', component_id='student_create')
        component.student_name = 'John Doe'
        component.student_age = 'veinte'
        component.student_email = 'john@example.com'
        component.student_note_1 = '85'
        component.student_note_2 = '90'
        component.student_note_3 = '88'
        
        with self.assertRaises(ValueError) as context:
            component.create_student()

        self.assertTrue('invalid literal for int() with base 10: \'veinte\'' in str(context.exception))
        

    # Funcional
    def test_check_avg(self):
        # Ingresar varios usuarios al mismo tiempo
        Student.objects.create(
            name="John Doea", age=20, email="john@example.com", note_1=85, note_2=90, note_3=88
        )
        Student.objects.create(
            name="Luis Alfredo", age=23, email="luis@example.com", note_1=90, note_2=90, note_3=90
        )
        Student.objects.create(
            name="Miguel David", age=22, email="miguel@example.com", note_1=90, note_2=80, note_3=95
        )
        component = StudentListView(component_name='student_list', component_id='student_list')
        component.mount()
        self.assertEqual(component.avg_age, 22.666666666666668)
        self.assertEqual(component.avg_note_1, 85.33333333333333)
        self.assertEqual(component.avg_note_2, 81.66666666666667)
        self.assertEqual(component.avg_note_3, 96)



    # Rendimiento
    def test_student_creation_multiple(self):
        num_users = 1000  # Número de usuarios a crear
        start_time = time.time()

        for i in range(num_users):
            Student.objects.create(
                name=f'John Doea {i}',
                age=20,
                email=f'john{i}@example.com',
                note_1=85,
                note_2=90,
                note_3=88
            )
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(f'Tiempo transcurrido para crear {num_users} usuarios: {time_elapsed} segundos')
        print('# usuarios creados: '+ str(Student.objects.count()))



    #Aceptacion
    def test_student_edit(self):
            self.student.name = "John Doe"
            self.student.save()
            self.assertEqual(Student.objects.get(email="john@example.com").name, "Miguel")


    #Integración
    def test_student_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "John Doea")



    # Prueba unitaria
    def test_student_creation(self):
        student = Student.objects.create(
            name="John Doea",
            age=20,
            email="john@example.com",
            note_1=85,
            note_2=90,
            note_3=88
        )
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.email, "john@example.com")
        print('# usuarios creados: '+ str(Student.objects.count())) 

    #Integracion
    def test_student_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200) #¿ok?
        self.assertContains(response, self.student.name)


    # self.student = Student.objects.create(
    #             name="John Doe",
    #             age=20,
    #             email="john@example.com",
    #             note_1=85,
    #             note_2=90,
    #             note_3=88
    #         )