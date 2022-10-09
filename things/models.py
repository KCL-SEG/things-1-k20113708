from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(models.Model):
	name = models.TextField(max_length = 30)
	description = models.TextField()
	quantity = models.IntegerField()
