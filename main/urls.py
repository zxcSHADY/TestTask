from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('log', views.EnterEm),
    path('log_in', views.login),
    path('reg', views.registrs),
    path('menu_reg', views.menu_reg),
    path('edit', views.edit_menu),
    path('edit_applay', views.edAp),
]