from rest_framework import serializers
from .models import *


class emp_serializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'