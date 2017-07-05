from django.db import models

# Create your models here.

class books(models.Model):
	bookTitle = models.CharField(max_length=10)
	bpub_date = models.DateField()
	def __str__(self):
		return self.pk

class heros(models.Model):
	name = models.CharField(max_length=20)
	gender = models.BooleanField()
	content = models.CharField(max_length=100)






