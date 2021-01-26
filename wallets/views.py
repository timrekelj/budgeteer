from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from .models import Wallet

# Create your views here.

def overview(request):
    template = loader.get_template('wallets/overview.html')
    context = {
        'title' : 'Overview'
    }
    return HttpResponse(template.render(context, request))

class WalletListView(ListView):
    model = Wallet
    template_name = 'wallets/overview.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'wallets'