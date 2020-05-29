#chart/urls.py

from django.urls import path
from . import views

app_name = 'chart'

urlpatterns = [

    path('',views.chartListView.as_view(), name='chart_list'),
    path('<int:pk>/',views.chart_detail_view,name='chart_detail'),
    path('write/', views.chart_write_view,name='chart_write'),
    path('<int:pk>/edit/',views.chart_edit_view,name='chart_edit'),
    path('<int:pk>/delete/',views.chart_delete_view,name='chart_delete'),
] 