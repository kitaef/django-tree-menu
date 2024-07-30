from django.contrib import admin
from menu.models import Menu


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'named_url', 'parent')
    list_filter = ('name',)
    search_fields = ('name', 'url', 'named_url')
    ordering = ('name', 'id')


admin.site.register(Menu, MenuAdmin)