# Generated by Django 4.2 on 2024-11-01 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradeNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='Задолженность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.tradenetwork', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Звено сети',
                'verbose_name_plural': 'Звенья сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('release_date', models.DateField(verbose_name='Дата выхода продукта на рынок')),
                ('trade_network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.tradenetwork', verbose_name='Элемент торговой сети')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
