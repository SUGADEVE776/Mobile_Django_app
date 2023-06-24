from django.contrib import admin
from .models import *
from django.db.models import *

# Register your models here.




class emp_admin(admin.ModelAdmin):
    list_display = ("name","age","dob","employed")
    list_filter = ("employed",)
    fieldsets =(('none',{
        'fields' : ("name","employed")
    }),
         ('Important',{
        'fields' : ("age","dob")
    }))
    # pass
    

admin.site.register(employee,emp_admin)
