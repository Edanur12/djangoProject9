
from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting, UserProfile
from product.models import category, Product


# Create your views here.
def index(request):
    current_user=request.user
    user=UserProfile.objects.get(user_id=current_user.id)
    settings=Setting.objects.filter(pk=0)
    context = {
               'settings':settings,
               'user':user
               }
    return render(request,'user_profile.html',context)