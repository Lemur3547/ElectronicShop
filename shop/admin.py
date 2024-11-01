from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from shop.models import TradeNetwork, Product


# Register your models here.
@admin.action(description="Очистить задолженность")
def сlear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(TradeNetwork)
class TradeNetworkAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'country', 'city', 'street', 'house', 'supplier', 'debt',)
    list_display = ('name', 'email', 'country', 'city', 'street', 'house', 'supplier_link', 'debt',)
    list_display_links = ('name', 'supplier_link',)
    list_filter = ('city',)
    search_fields = ('city',)
    actions = (сlear_debt,)

    def supplier_link(self, obj):
        link = reverse("admin:shop_tradenetwork_change", args=[obj.supplier_id])
        return mark_safe(u'<a href="%s">%s</a>' % (link, TradeNetwork.objects.get(id=obj.supplier_id)))

    supplier_link.allow_tags = True
    supplier_link.short_description = 'Поставщик'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'model', 'release_date', 'trade_network')
    list_display = ('name', 'description', 'model', 'release_date', 'trade_network_link')
    list_display_links = ('name', 'trade_network_link', )
    search_fields = ('name',)

    def trade_network_link(self, obj):
        link = reverse("admin:shop_tradenetwork_change", args=[obj.trade_network_id])
        return mark_safe(u'<a href="%s">%s</a>' % (link, TradeNetwork.objects.get(id=obj.trade_network_id)))

    trade_network_link.allow_tags = True
    trade_network_link.short_description = 'Элемент торговой сети'

