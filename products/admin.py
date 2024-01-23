from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date_release', 'owner', 'pk')
    list_filter = ('owner', 'date_release')
    search_fields = ('owner', 'name', 'model', 'date_release')
