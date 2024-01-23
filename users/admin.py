from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'role', 'is_active', 'pk')
    list_filter = ('role', 'is_active',)
