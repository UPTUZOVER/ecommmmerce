from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category
from parler.admin import TranslatableAdmin

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('title', 'updated_on', 'created_on')
    search_fields = ('translations__title',)
    list_filter = ('updated_on', 'created_on')
    readonly_fields = ('created_on', 'updated_on')
