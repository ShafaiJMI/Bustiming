from django.db import models

# Create your models here.
class BusTiming(models.Model):
	name = models.CharField(max_length=50)
	latitude = models.FloatField(default=0.0000)
	longitude = models.FloatField(default=0.0000)
	time = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)