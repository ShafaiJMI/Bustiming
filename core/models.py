from django.db import models

# Create your models here.
class Bus(models.Model):
	bus_number = models.CharField(max_length=10)
	bus_uid = models.CharField(max_length=10)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.bus_number+ "-" + self.bus_uid)

class BusStop(models.Model):
	name = models.CharField(max_length=50)
	latitude = models.FloatField(default=0.0000)
	longitude = models.FloatField(default=0.0000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class BusTiming(models.Model):
	bus = models.ForeignKey(Bus,on_delete=models.CASCADE,null=True,blank=True)
	busstop = models.ForeignKey(BusStop,on_delete=models.CASCADE,null=True,blank=True)
	time = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)