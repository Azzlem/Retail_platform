from django.db import models
from django.utils import timezone

from config.settings import NULLABLE
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Product Name")
    model = models.CharField(max_length=150, verbose_name="Product Model")
    date_release = models.DateField(verbose_name="Date Released", default=timezone.now)

    owner = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['-date_release']