from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from shop.models import Product, TradeNetwork
from shop.serializers import ProductSerializer, TradeNetworkSerializer, TradeNetworkUpdateSerializer


# Create your views here.
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class TradeNetworkCreateAPIView(generics.CreateAPIView):
    serializer_class = TradeNetworkSerializer
    permission_classes = [IsAuthenticated]


class TradeNetworkListAPIView(generics.ListAPIView):
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('country', )
    permission_classes = [IsAuthenticated]


class TradeNetworkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated]


class TradeNetworkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TradeNetworkUpdateSerializer
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated]


class TradeNetworkDestroyAPIView(generics.DestroyAPIView):
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated]
