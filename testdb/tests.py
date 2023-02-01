from django.test import TestCase
from testdb.models import Teacher, Subject

# Create your tests here.

class TeacherTestCase(TestCase):


    def setUp(self):

        self.physics = Subject(name="Physics")
        self.physics.save()

        t1 = Teacher(name="Niels Bohr", age=46)
        t1.save()
        t1.subject.add(self.physics)
        t1.save()

    def test_teacher(self):
        self.assertEqual(Teacher.objects.filter(name="Niels Bohr")[0].age, 46)
        self.assertEqual(Subject.objects.filter(name="Physics")[0].name, "Physics")
        self.assertEqual(Teacher.objects.filter(name="Niels Bohr")[0].subject.all()[0], self.physics)
