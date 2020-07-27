from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.

def index(request):
    return HttpResponse("<h1>views of myapp</h1>")

def home(request):
    return render(request,"myapp/home.html",{'name':"jyothi"})

def fact(request,f):
    f=int(f)
    return HttpResponse("factorial is :  {}".format(factorial(f)))

def child(request):
    return render(request,"child.html")