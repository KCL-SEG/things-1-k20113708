from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(models.Model):
	name = models.CharField(unique = True, blank = False, max_length = 31)
	description = models.CharField(unique = False, blank = True, max_length = 121)
	quantity = models.IntegerField(unique = False, validators=[MaxValueValidator(100),MinValueValidator(0)])
