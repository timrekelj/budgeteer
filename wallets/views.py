from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
    DeleteView
)
from .models import Wallet

# Create your views here.

class WalletListView(ListView):
    model = Wallet
    template_name = 'wallets/overview.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'wallets'

class WalletDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Wallet

    def test_func(self):
        wallet = self.get_object()
        if self.request.user == wallet.owner:
            return True
        return False

class WalletCreateView(LoginRequiredMixin, CreateView):
    model = Wallet
    fields = ['title', 'value']

    def form_valid(self, form):
    	form.instance.owner = self.request.user 
    	return super().form_valid(form)

class WalletDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wallet
    success_url = '/wallets/overview'

    def test_func(self):
        wallet = self.get_object()
        if self.request.user == wallet.owner:
            return True
        return False
