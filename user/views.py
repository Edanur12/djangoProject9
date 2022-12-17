
from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting, UserProfile
from product.models import category


# Create your views here.
def index(request):
    if request.user.id is not None:
        Category = category.objects.all()
        user = UserProfile.objects.get(user_id=request.user.id)
        settings = Setting.objects.filter(pk=0)
        context = {'category': Category,
                   'user': user,
                   'settings': settings}
        return render(request, 'user_profile.html', context)