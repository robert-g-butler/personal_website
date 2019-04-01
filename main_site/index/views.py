
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(
        request=request, template_name='index/home.html', context={}
    )

def about(request):
    return render(
        request=request, template_name='index/about.html', context={}
    )