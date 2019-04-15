
from django.shortcuts import render

def index(request):
    '''Returns the render for the website main page.'''
    return render(
        request=request, template_name='index/home.html', context={}
    )

def about(request):
    '''Returns the render for the website "About" page.'''
    return render(
        request=request, template_name='index/about.html', context={}
    )

def contact(request):
    '''Returns the render for the website "Contact" page.'''
    return render(
        request=request, template_name='index/contact.html', context={}
    )
