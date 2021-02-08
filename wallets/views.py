from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
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

from django.db.models import F

# Create your views here.

class WalletListView(ListView):
    model = Wallet
    template_name = 'wallets/overview.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'wallets'

def addValue(request):
    if request.GET.get('addValue'):
        profil = get_object_or_404(Wallet, created_by=request.user)
        profil.value = F('value') + 10
        profil.save(update_fields=["value"])
        return render(request, 'wallets/wallet_detail.html')

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

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all().order_by('title')
    serializer_class = WalletSerializer