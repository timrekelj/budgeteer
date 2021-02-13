from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from decimal import Decimal
#from rest_framework import viewsets
from django.urls import reverse
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
    DeleteView
)
from .models import Wallet
from .serializers import WalletSerializer

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

def changeValue(request, pk):
    value = request.POST.get('value')
    wallet = get_object_or_404(Wallet, pk=pk)
    wallet.value += Decimal(value)
    wallet.save()
    return redirect('wallet-detail', pk=wallet.pk)


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

# class WalletViewSet(viewsets.ModelViewSet):
#     queryset = Wallet.objects.all().order_by('title')
#     serializer_class = WalletSerializer