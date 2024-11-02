from rest_framework import serializers

from shop.models import Product, TradeNetwork
from shop.validators import DebtUpdateValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class TradeNetworkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, source='product_set', read_only=True)

    class Meta:
        model = TradeNetwork
        fields = '__all__'


class TradeNetworkUpdateSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, source='product_set', read_only=True)

    class Meta:
        model = TradeNetwork
        fields = '__all__'
        validators = [DebtUpdateValidator('debt')]
