from django.db import models
from Apps.core.models import Profile

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.IntegerField()
    semestre = models.IntegerField()
    carrera = models.CharField(max_length=5)
    liberado = models.BooleanField(default=False)
    date_enrollment = models.DateTimeField(auto_now_add==True)

class Team(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = model.CharField(max_length=25)
    max_students = models.IntegerField()
    schedule = models.CharField(max_length=50)
    place = models.CharField(max_length=25)

