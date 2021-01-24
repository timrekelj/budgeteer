from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def overview(request):
    template = loader.get_template('wallets/overview.html')
    context = {
        'title' : 'Overview'
    }
    return HttpResponse(template.render(context, request))
