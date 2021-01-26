from django.urls import path
from .views import WalletListView
from . import views

urlpatterns = [
    path('overview', WalletListView.as_view(), name='overview'),
]
