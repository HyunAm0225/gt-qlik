from django.contrib import admin
from .models import Chart
# Register your models here.

class ChartAdmin(admin.ModelAdmin):
    list_displayy = (
        'chart_rank',
        'chart_title',
        'chart_url',
        'chart_register',
    )
    search_fields = ('chart_title','chart_url','chart_writer__user_id',)

admin.site.register(Chart,ChartAdmin)
