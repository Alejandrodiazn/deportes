from django.db import models
from django.contrib.auth.models import User

""" 
Docentes:
Foto
Descripción
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/')
    desc = models.TextField()
