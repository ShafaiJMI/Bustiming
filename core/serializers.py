from rest_framework import serializers
from .models import BusTiming
from django.contrib.auth.models import User

class TimeSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusTiming
		fields = ['id','name','time',]

class StopSerializer(serializers.ModelSerializer):
	class Meta:
		model = BusTiming
		fields = ['id','name','latitude','longitude','created_at','updated_at']