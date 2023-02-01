
import os, sys
appname = "postgresTest"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", appname+".settings")
import django
django.setup()

from testdb.models import Teacher, Subject

physics = Subject.objects.create(name="Physics")

t1 = Teacher.objects.create(name="Niels Bohr", age=46)
t1.subject.add(physics)
t1.save()

