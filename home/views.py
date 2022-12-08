
from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product, category


# Create your views here.

def index(request):
    Category=category.objects.all()
    context = {'category': Category}
    return render(request,'index.html',context)

def category_products(request, id, slug):
    Category = category.objects.all()
    selectedCategory = category.objects.filter(pk=id)
    product = Product.objects.filter(category_id=id)
    context = {'selectedCategory': selectedCategory,
               'Products': product,
               'category':Category}
    return render(request, 'category_products.html', context)