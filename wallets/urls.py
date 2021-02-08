from django.urls import path
from .views import (
	WalletListView,
	WalletCreateView,
	WalletDeleteView
)
from . import views

urlpatterns = [
    path('overview/', WalletListView.as_view(), name='overview'),
    path('new/', WalletCreateView.as_view(), name='wallet-create'),
    #path('<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),
    path('<int:pk>/delete', WalletDeleteView.as_view(), name='wallet-delete'),
]
