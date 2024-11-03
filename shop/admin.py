from django.contrib import admin
from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.safestring import mark_safe

from shop.models import TradeNetwork, Product


# Register your models here.
@admin.action(description="Очистить задолженность")
def clear_debt(modeladmin, request, queryset):
    """Admin action для очистки задолженности перед поставщиком"""
    queryset.update(debt=0)


@admin.register(TradeNetwork)
class TradeNetworkAdmin(admin.ModelAdmin):
    """Регистрация модели элемента сети в админке"""
    fields = ('name', 'email', 'type', 'country', 'city', 'street', 'house', 'supplier', 'debt',)
    list_display = ('name', 'email', 'type', 'country', 'city', 'street', 'house', 'supplier_link', 'debt',)
    list_display_links = ('name', 'supplier_link',)
    list_filter = ('city',)
    search_fields = ('city',)
    actions = (clear_debt,)

    def supplier_link(self, obj):
        """Функция для реализации ссылки на поставщика у записи элемента торговой сети в админке"""
        link = reverse("admin:shop_tradenetwork_change", args=[obj.supplier_id])
        return mark_safe(u'<a href="%s">%s</a>' % (link, TradeNetwork.objects.get(id=obj.supplier_id)))

    supplier_link.allow_tags = True
    supplier_link.short_description = 'Поставщик'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Регистрация модели продукта в админке"""
    fields = ('name', 'description', 'model', 'release_date', 'trade_network')
    list_display = ('name', 'get_description', 'model', 'release_date', 'trade_network_link')
    list_display_links = ('name', 'trade_network_link', )
    search_fields = ('name',)

    def trade_network_link(self, obj):
        """Ссылка на элемент торговой сети, к которой этот продукт относится"""
        link = reverse("admin:shop_tradenetwork_change", args=[obj.trade_network_id])
        return mark_safe(u'<a href="%s">%s</a>' % (link, TradeNetwork.objects.get(id=obj.trade_network_id)))

    def get_description(self, obj):
        return truncatechars(obj.description, 100)

    trade_network_link.allow_tags = True
    trade_network_link.short_description = 'Элемент торговой сети'
    get_description.short_description = 'Описание'
