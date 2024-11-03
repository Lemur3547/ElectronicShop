from django.urls import path

from shop.apps import ShopConfig
from shop.views import ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView, TradeNetworkListAPIView, TradeNetworkCreateAPIView, \
    TradeNetworkRetrieveAPIView, TradeNetworkUpdateAPIView, TradeNetworkDestroyAPIView

app_name = ShopConfig.name

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('product/create/', ProductCreateAPIView.as_view(), name='create_product'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='view_product'),
    path('product/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', ProductDestroyAPIView.as_view(), name='delete_product'),

    path('trade_network/', TradeNetworkListAPIView.as_view(), name='trade_network'),
    path('trade_network/create/', TradeNetworkCreateAPIView.as_view(), name='create_trade_network'),
    path('trade_network/<int:pk>/', TradeNetworkRetrieveAPIView.as_view(), name='view_trade_network'),
    path('trade_network/<int:pk>/update/', TradeNetworkUpdateAPIView.as_view(), name='update_trade_network'),
    path('trade_network/<int:pk>/delete/', TradeNetworkDestroyAPIView.as_view(), name='delete_trade_network'),
]
