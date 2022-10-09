from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(models.Model):
	name = models.TextField(unique = True)
	description = models.TextField(unique = False)
	quantity = models.IntegerField(unique = False)
