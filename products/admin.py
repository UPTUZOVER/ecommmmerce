from django.contrib import admin
from .models import Product
from parler.admin import TranslatableAdmin

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('title', 'price', 'count', 'updated_on')
    search_fields = ('translations__title', 'translations__description')
    list_filter = ('categories', 'updated_on')
    readonly_fields = ('created_on', 'updated_on')
