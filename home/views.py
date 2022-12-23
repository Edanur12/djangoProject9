from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.forms import NewUserForm
from home.models import Setting, UserProfile
from product.models import Product, category, Images, Comment


# Create your views here.
def index(request):
    Category = category.objects.all()
    settings = Setting.objects.filter(pk=0)
    sliderData = Product.objects.all()[:6]
    dayproducts = Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[0:4]
    randomproducts = Product.objects.all().order_by('?')[0:4]
    context = {'category': Category,
               'sliderData': sliderData,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts,
               'settings': settings,
               }
    return render(request, 'index.html', context)


def category_products(request, id, slug):
    Category = category.objects.all()
    selectedCategory = category.objects.filter(pk=id)
    product = Product.objects.filter(category_id=id)
    context = {'selectedCategory': selectedCategory,
               'Products': product,
               'category':Category}
    return render(request, 'category_products.html', context)
def product_detail(request,id,slug):
    comment = Comment.objects.filter(product_id=id, status='True')
    Category = category.objects.all()
    products = Product.objects.filter(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {'products': products,
               'comments': comment,
               'category': Category,
               'images': images}
    return render(request, 'product_detail.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    Category = category.objects.all()
    context = {'category': Category, }
    return render(request, 'login.html', context)
def logout_view(request):
    url=request.META.get('HTTP_REFERER')
    logout(request)
    return HttpResponseRedirect(url)

def signup_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.save()
            return HttpResponseRedirect('/')
    form = NewUserForm()
    Category = category.objects.all()
    context = {'category': Category,
               'form': form, }
    return render(request, 'signup_view.html', context)