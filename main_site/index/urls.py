
from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index-home'),
    path(route='about/', view=views.about, name='index-about'),
]

