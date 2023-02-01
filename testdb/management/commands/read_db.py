from django.core.management.base import BaseCommand, CommandError

from testdb.models import Teacher, Subject


class Command(BaseCommand):

    help = 'reads db'

    def add_argument(self, parser):
        pass

    def handle(self, *args, **kwargs):
        print("reading DB")
        try:
            print(Subject.objects.all())
            print(Teacher.objects.all())
        except:
            print("problem reading db")
