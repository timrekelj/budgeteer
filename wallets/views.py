from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Wallet

# Create your views here.

class WalletListView(ListView):
    model = Wallet
    template_name = 'wallets/overview.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'wallets'

class WalletDetailView(DetailView):
    model = Wallet