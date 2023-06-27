from django.contrib import admin
from .models import *

# Register your models here.


class traveladmin(admin.ModelAdmin):
    list_display = ['name','desc','image','offer']

admin.site.register(travel,traveladmin)