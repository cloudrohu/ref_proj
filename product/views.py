from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Max, Min
from django.contrib.auth import authenticate,logout,login

# Create your views here.


def PRODUCT(request):  
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    product = Product.objects.all()
    brand = Brand.objects.all()
    color = Color.objects.all()

    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    print(min_price)
    print(max_price)

    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)
    else:
        product = Product.objects.all()

    ColorID = request.GET.get('colorID')
    if ColorID:
        product = Product.objects.filter(color=ColorID)
    else:
        product = Product.objects.all()

        
    context = {
        'category': category,
        'product': product,
        'color': color,
        'brand': brand,
        'sub_category': sub_category,
        'min_price':min_price,
        'max_price':max_price,
	    'FilterPrice':FilterPrice,
        
    }
    return render(request, 'product/product/product.html',context)


def product_details(request,slug): 

    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.get(slug = slug)
    else :
        return redirect('404')
    context = {

        'product': product,
    }   
     
    return render(request, 'product/product_detail.html',context)


def filter_data(request):
    categories = request.GET.getlist('sub_category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(Categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(Brand__id__in=brands).distinct()


    t = render_to_string('ajax/product.html', {'product': allProducts})

    return JsonResponse({'data': t})