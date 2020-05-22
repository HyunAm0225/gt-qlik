#menu/urls.py

from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [

    path('',views.MenuListView.as_view(), name='menu_list'),

] 