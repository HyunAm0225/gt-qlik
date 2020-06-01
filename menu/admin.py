from django.contrib import admin
from .models import Menu
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


# Register your models here.

class MenuAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'menu_rank',
        'writer',
        'title',
        'url',
    )
    search_fields = ('menu_rank','title','writer',)

admin.site.register(Menu,MenuAdmin)
