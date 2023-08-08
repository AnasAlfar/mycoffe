from django.shortcuts import  get_object_or_404,render
from django.http import HttpResponse
from . models import product



# Create your views here.

def products(request):
    pro=product.objects.all()
    name=None 
    desc=None
    pfrom=None
    pto=None
    
    if 'searchname' in request.GET:
        name=request.GET['searchname']
        if name:
            pro=pro.filter(name__icontains=name)
    if 'searchdesc' in request.GET:
        desc=request.GET['searchname']
        if desc:
            pro=pro.filter(description__icontains=desc)
    if 'searchpricefrom' in request.GET and 'searchpriceto' in request.GET:
        pfrom=request.GET['searchpricefrom']
        pto=request.GET['searchpriceto']
        if pfrom and pto:
            if pfrom.isdigit() and pto.isdigit():
                pro=pro.filter(price__gte=pfrom,price__lte=pto)




    x={"pro":pro}
    return render(request,'products/products.html',x)

def productt(request,pro_id):
    x={"pro":get_object_or_404(product,pk=pro_id)}
    return render(request,'products/product.html',x)


def search(request):
    return render(request,'products/search.html')