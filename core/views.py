from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import TimeSerializer,StopSerializer,BusSerializer
from .models import BusTiming,BusStop,Bus
from rest_framework.views import APIView

# Create your views here.
def index(request):
	return render(request,'index.html')

class TimeView(APIView):
	def get(self,request):
		queryset = BusTiming.objects.all()
		serializer = TimeSerializer(queryset,many=True)
		return JsonResponse(serializer.data,safe=False)

class StopTiming(APIView):
	def get(self,request,pk):
		queryset = BusTiming.objects.get(pk=pk)
		serializer = TimeSerializer(queryset)
		return JsonResponse(serializer.data,safe=False)

class StopView(APIView):
	def get(self,request):
		queryset = BusStop.objects.all()
		serializer = StopSerializer(queryset,many=True)
		return JsonResponse(serializer.data,safe=False)

class BusView(APIView):
	def get(self,request):
		queryset = Bus.objects.all()
		serializer = BusSerializer(queryset,many=True)
		return JsonResponse(serializer.data,safe=False)