from django.contrib import admin
from .models import Keyword, Job


class JobUrl(admin.ModelAdmin):
    list_display = ['id', 'url']


class KeywordEditor(admin.ModelAdmin):
    list_display = ['id', 'keyword', 'created_at']
    ordering = ['id']


admin.site.register(Keyword, KeywordEditor)
admin.site.register(Job, JobUrl)
