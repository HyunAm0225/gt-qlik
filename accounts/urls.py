from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('pw/', views.RecoveryPwView.as_view(), name='recovery_pw'),
    path('pw/find/', views.ajax_find_pw_view, name='ajax_pw'),
    path('pw/auth/', views.auth_confirm_view, name='recovery_auth'),
    path('pw/reset/', views.auth_pw_reset_view, name='recovery_pw_reset'),

]