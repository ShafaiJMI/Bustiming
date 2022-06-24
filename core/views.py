#from django.shortcuts import render
#from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TimeSerializer,StopSerializer
from .models import BusTiming
#from django.contrib.auth.models import User
# Create your views here.
class StopTiming(APIView):
	def get(self,request,pk):
		queryset = BusTiming.objects.get(pk=pk)
		serializer = StopSerializer(queryset)
		return Response(serializer.data)
class StopView(APIView):
	def get(self,request):
		queryset = BusTiming.objects.all()
		serializer = StopSerializer(queryset,many=True)
		return Response(serializer.data)
class TimeView(APIView):
	def get(self,request):
		queryset = BusTiming.objects.all()
		serializer = TimeSerializer(queryset,many=True)
		return Response(serializer.data)