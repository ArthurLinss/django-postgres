from django.core.management.base import BaseCommand, CommandError

from testdb.models import Teacher, Subject


class Command(BaseCommand):

    help = 'fill db with dummies'

    def add_argument(self, parser):
        pass

    def handle(self, *args, **kwargs):

        print("filling db")

        physics = Subject.objects.create(name="Physics")

        t1 = Teacher.objects.create(name="Niels Bohr", age=46)
        t1.subject.add(physics)
        t1.save()

