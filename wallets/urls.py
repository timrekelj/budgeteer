from django.urls import path
from .views import WalletListView, WalletDetailView
from . import views

urlpatterns = [
    path('overview/', WalletListView.as_view(), name='overview'),
    path('<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),
]
