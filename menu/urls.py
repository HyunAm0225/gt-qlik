#menu/urls.py

from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [

    path('',views.MenuListView.as_view(), name='menu_list'),
    path('<int:pk>/',views.menu_detail_view,name='menu_detail'),
    path('write/', views.menu_write_view,name='menu_write'),
    path('<int:pk>/edit/',views.menu_edit_view,name='menu_edit'),
    path('<int:pk>/delete/',views.menu_delete_view,name='menu_delete'),
] 