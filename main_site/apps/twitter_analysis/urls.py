from django.urls import path

from . import views

urlpatterns = [
    path(route='', view=views.index, name='twitter-index'),
    path(route='user_report/', view=views.user_report, name='user-report'),
    path(route='global_trends/', view=views.global_trends,
         name='global-trends'),
]