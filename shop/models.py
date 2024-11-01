from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class TradeNetwork(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(max_length=255, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Номер дома')
    supplier = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.SET_NULL, **NULLABLE)
    debt = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Задолженность', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    model = models.CharField(max_length=50, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    trade_network = models.ForeignKey(TradeNetwork, verbose_name='Элемент торговой сети', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
