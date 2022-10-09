from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(models.Model):
	name = models.CharField(max_length = 30)
	description = models.CharField(max_length = 120, blank = True, unique = False)
	quantity = models.IntegerField(validators = [MaxValueValidator(100), MinValueValidator(0)], unique = False)
