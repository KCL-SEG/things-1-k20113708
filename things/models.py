from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(models.Model):
	name = models.CharField(max_length = 31)
	description = models.CharField(max_length = 121)
	quantity = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
