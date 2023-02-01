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
    subject = models.ManyToManyField(Subject, default=None)


    def __str__(self):
        return self.name

    def __iter__(self):
        """
        for all model fields get value. usage:
        $ for field, val in model_instance:
        $    print(field, val)
        """
        for field in self._meta.get_fields():
            yield (field.name, field.value_from_object(self))
