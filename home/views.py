from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('home/index.html')
    context = {
        'title' : 'Home'
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
def error_404(request, exception):
    template = loader.get_template('home/404.html')
    context = {
        'title' : '404'
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
def error_403(request, exception):
    template = loader.get_template('home/403.html')
    context = {
        'title' : '403'
    }
    return HttpResponse(template.render(context, request))


def error_400(request, exception):
    template = loader.get_template('home/400.html')
    context = {
        'title' : '400'
    }
    return HttpResponse(template.render(context, request))


def error_500(request, exception):
    template = loader.get_template('home/500.html')
    context = {
        'title' : '500'
    }
    return HttpResponse(template.render(context, request))
