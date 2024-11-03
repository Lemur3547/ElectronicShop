from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from shop.models import Product, TradeNetwork
from shop.serializers import ProductSerializer, TradeNetworkSerializer, TradeNetworkUpdateSerializer


# Create your views here.
class ProductCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания продукта"""
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductListAPIView(generics.ListAPIView):
    """Контроллер для вывода списка продуктов"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для изменения продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления продукта"""
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class TradeNetworkCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания элемента торговой сети"""
    serializer_class = TradeNetworkSerializer
    permission_classes = [IsAuthenticated]


class TradeNetworkListAPIView(generics.ListAPIView):
    """Контроллер для вывода списка элементов торговой сети"""
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('country', )
    permission_classes = [IsAuthenticated]


class TradeNetworkRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра элемента торговой сети"""
    serializer_class = TradeNetworkSerializer
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated]


class TradeNetworkUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для изменения элемента торговой сети"""
    serializer_class = TradeNetworkUpdateSerializer
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated]


class TradeNetworkDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления элемента торговой сети"""
    queryset = TradeNetwork.objects.all()
    permission_classes = [IsAuthenticated]
