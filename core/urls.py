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
    path('timing/', views.TimeView.as_view()),
    path('timing/<int:pk>/', views.StopTiming.as_view()),
    path('stops/', views.StopView.as_view()),
]