from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from ecomm.models import product
from django.contrib.auth import *

def index(request):
    products=product.objects.all()
    print(products)
    # print(a)

    alpha = {'hello':products}
    return render(request,'bootss.html',alpha)


