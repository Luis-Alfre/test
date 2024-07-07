from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    note_1 = models.IntegerField(default=0)
    note_2 = models.IntegerField(default=0)
    note_3 = models.IntegerField(default=0)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

    