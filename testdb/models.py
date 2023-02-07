from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=80, unique=True)
    #user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
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

class Book(models.Model):


    GENRE_CHOICES = (
        ("Thriller", "Thriller"),
        ("Science", "Science"),
    )

    title = models.CharField(max_length=144, unique=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    number_of_pages = models.PositiveBigIntegerField(default=0)
    genre = models.CharField(max_length=100,choices = GENRE_CHOICES, default=None, null=True)

    def __str__(self):
        return self.title