from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    employed = models.BooleanField()

    class Meta:
        db_table = 'Employee'
