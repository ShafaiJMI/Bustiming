from django.urls import path,include
from rest_framework import routers
from . import views
'''
router = routers.DefaultRouter()
router.register(r'timing', views.TimeViewSet)
router.register(r'stops', views.StopViewSet)
'''
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',views.index,name="home"),
    path('timing/', views.TimeView.as_view(),name="timing"),
    path('timing/<int:pk>/', views.StopTiming.as_view(),name="busstop_timing"),
    path('stops/', views.StopView.as_view(),name="stop"),
    path('Bus/', views.BusView.as_view(),name="bus"),
]