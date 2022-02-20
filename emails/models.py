from django.db import models

# Create your models here.

class Querie(models.Model):
  fname = models.CharField(max_length=20, blank=False)
  lname = models.CharField(max_length=20, blank=False)
  email = models.EmailField(blank=False)
  QueryDesc = models.CharField(max_length=2000)
  DateTime = models.DateTimeField(auto_now_add=True)