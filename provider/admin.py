from django.contrib import admin
from provider.models import Provider


@admin.action(description="Очистить задолженность перед поставщико")
def debt_zero(modeladmin, request, queryset):
    queryset.update(debt=0)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('provide', 'name', 'city', 'levels', 'debt',)
    actions = [debt_zero]
    list_filter = ('city',)


admin.site.register(Provider, ArticleAdmin)
