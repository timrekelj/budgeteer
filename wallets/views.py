from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import (
	ListView,
	DetailView,
	CreateView
)
from .models import Wallet

# Create your views here.

class WalletListView(ListView):
    model = Wallet
    template_name = 'wallets/overview.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'wallets'

class WalletDetailView(DetailView):
    model = Wallet

class WalletCreateView(CreateView):
    model = Wallet
    fields = ['title', 'value']

    def form_valid(self, form):
    	form.instance.owner = self.request.user 
    	return super().form_valid(form)

