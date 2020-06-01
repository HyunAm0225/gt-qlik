from django.contrib import admin
from .models import Chart
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

# Register your models here.

class ChartAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'chart_rank',
        'chart_writer',
        'chart_title',
        'chart_url',
        'chart_register',
    )
    search_fields = ('chart_title','chart_url','chart_writer',)

admin.site.register(Chart,ChartAdmin)


