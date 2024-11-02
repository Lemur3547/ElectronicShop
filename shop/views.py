from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from shop.models import Product, TradeNetwork
from shop.serializers import ProductSerializer, TradeNetworkSerializer, TradeNetworkUpdateSerializer


# Create your views here.
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()


class TradeNetworkCreateAPIView(generics.CreateAPIView):
    serializer_class = TradeNetworkSerializer


class TradeNetworkListAPIView(generics.ListAPIView):
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('country', )


class TradeNetworkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()


class TradeNetworkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TradeNetworkUpdateSerializer
    queryset = TradeNetwork.objects.all()


class TradeNetworkDestroyAPIView(generics.DestroyAPIView):
    queryset = TradeNetwork.objects.all()
