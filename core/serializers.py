from rest_framework import serializers
from .models import BusTiming,BusStop,Bus

class TimeSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusTiming
		fields = ['id','bus','busstop','time',]

class StopSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusStop
		fields = ['id','name','latitude','longitude','created_at','updated_at']

class BusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus
		fields = ['id','bus_number','created_at','updated_at']