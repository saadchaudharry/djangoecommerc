from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import product

# Create your views here.
def index(request):
    # products=product.objects.all()
    # print(products)
    # n=len(products)
    # nSlide= n//4 + ceil((n/4)-(n//4))
    allprod=[]
    catprod=product.objects.values('catagory')
    cats={item['catagory'] for item in catprod }
    for cat in cats:
        prod=product.objects.filter(catagory=cat)
        n = len(prod)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allprod.append([prod,range(1,nSlide),nSlide])


    # params={'no_of_slide':nSlide,'product':products,'range':range(1,nSlide)}
    # allprod=[[products,range(1,nSlide),nSlide],
    #          [products,range(1,nSlide),nSlide]]
    params={'allprod':allprod}
    return render(request,'shop/indexx.html',params)

def about(request):
    return render(request,'shop/about.html')

def Tracker(request):
    return HttpResponse('tracker')

def productt(request, myid):
    Product=product.objects.filter(id =myid)
    print(Product)

    return render(request,'shop/prodview.html',{'product':Product})

def search(request):
    return HttpResponse('search')

def contact(request):
    return HttpResponse('contact')
