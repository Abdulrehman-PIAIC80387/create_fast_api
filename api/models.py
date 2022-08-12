from django.db import models

# Create your models here.
class Address (models.Model):
 firstname = models.CharField(max_length=100)
 auth = models.CharField(max_length=100)
 userId = models.CharField(max_length=100)
 HashId = models.CharField(max_length=100)
