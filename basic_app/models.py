from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={'pk':self.pk})

 
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveBigIntegerField()
    School = models.ForeignKey(School,related_name='students', on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name
