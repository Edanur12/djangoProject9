from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    text = "merhaba dunya"
    return HttpResponse(text)
    context = {'text2': text}
    return render(request, 'index.html', context)
