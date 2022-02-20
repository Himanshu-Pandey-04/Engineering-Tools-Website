from django.db import models
from emails.models import Querie
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
  Middle_Name = models.CharField(max_length=16, blank=True)
  queries = models.ManyToManyField(Querie, blank=True)

  def __str__(self):
    return f'{self.first_name} {self.last_name} ({self.username})'