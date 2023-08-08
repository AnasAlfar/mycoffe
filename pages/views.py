from django.shortcuts import render
from django.http import HttpResponse
from products.models import product

# Create your views here.

def index(request):
    x={"pro":product.objects.all()}
    return render(request, 'pages/index.html',x)

def about(request):
    return render(request, 'pages/about.html')


def coffe(request):
    return render(request,'pages/coffe.html')
    