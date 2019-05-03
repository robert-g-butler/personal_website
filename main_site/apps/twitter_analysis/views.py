from django.shortcuts import render

def index(request):
    return render(request=request,
                  template_name='twitter_analysis/index.html',
                  context={})

def user_report(request):
    return render(request=request,
                  template_name='twitter_analysis/user_report.html',
                  context={})

def global_trends(request):
    return render(request=request,
                  template_name='twitter_analysis/global_trends.html',
                  context={})

