from django.contrib import admin

# Register your models here.
from .models import BusTiming,BusStop,Bus
admin.site.register(BusTiming)
admin.site.register(Bus)
admin.site.register(BusStop)