from rest_framework import serializers

from .models import Wallet

class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Wallet:
        model = Wallet
        fields = ('title', 'value', 'date_created', 'owner')