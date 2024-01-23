from django.db import models
from django.utils import timezone

from config.settings import NULLABLE
from products.models import Product
from users.models import User


class Levels(models.IntegerChoices):
    FACTORY = 0, 'Завод'
    RETAIL = 1, 'Розничная сеть'
    IP = 2, 'Индивидуальный предприниматель'


class Provider(models.Model):

    product = models.ManyToManyField(Product, verbose_name='Продукт')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поставщика', **NULLABLE)
    provide = models.ForeignKey('Provider', on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)

    name = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    country = models.CharField(max_length=200, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house = models.CharField(max_length=100, verbose_name='Номер дома')

    levels = models.IntegerField(choices=Levels.choices, default=Levels.FACTORY, verbose_name='Уровень структуры')
    debt = models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Задолженность', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('city',)
