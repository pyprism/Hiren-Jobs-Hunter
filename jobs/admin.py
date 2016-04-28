from django.contrib import admin
from .models import Keyword


class KeywordEditor(admin.ModelAdmin):
    list_display = ['id', 'keyword', 'created_at']
    ordering = ['id']


admin.site.register(Keyword, KeywordEditor)
