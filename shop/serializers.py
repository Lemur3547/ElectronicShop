from rest_framework import serializers

from shop.models import Product, TradeNetwork
from shop.validators import DebtUpdateValidator


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукта"""
    class Meta:
        model = Product
        fields = '__all__'


class TradeNetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели звена торговой сети"""
    products = ProductSerializer(many=True, source='product_set', read_only=True)

    class Meta:
        model = TradeNetwork
        fields = '__all__'


class TradeNetworkUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для изменения звена торговой сети. При изменении объекта запрещено менять задолженность"""
    products = ProductSerializer(many=True, source='product_set', read_only=True)

    class Meta:
        model = TradeNetwork
        fields = '__all__'
        validators = [DebtUpdateValidator('debt')]
