from django.db import models

# Create your models here.

from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    subject = models.ManyToManyField(Subject)


    def __str__(self):
        return self.name
