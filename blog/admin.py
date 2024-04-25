from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date',)
    list_display = ('pk','title','text','creation_date','published','view_count')
    list_filter = ('published','view_count')
    search_fields = ('text','title')
