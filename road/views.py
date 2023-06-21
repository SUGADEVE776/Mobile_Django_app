from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from django.http import HttpResponse

def index(val):
    a =  "Hello World"
    return a * val

def count(x):
    c = x*5
    a = fact(a=c)
    return a


class kowsi(APIView):
    def get(self,request):
        data = index()
        return Response(data)

    def post(self,request):
        data = request.data
        c = data['input']
        result = count(x=c)
        return Response(result)


def fact(a):
    c = a*10
    z = index(val = c)
    return c,z