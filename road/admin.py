from django.contrib import admin
from .models import *
from django.db.models import *

# Register your models here.




class emp_admin(admin.ModelAdmin):
    list_display = ("name","age","dob","employed","show_average")
    list_filter = ("employed",)
    fieldsets =(('none',{
        'fields' : ("name","employed")
    }),
         ('Important',{
        'fields' : ("age","dob")
    }))
    # pass
    def show_average(self, obj):
        from django.db.models import Avg
        result = employee.objects.filter(name=obj).aggregate(Avg("age"))
        return result["age__avg"]

admin.site.register(employee,emp_admin)