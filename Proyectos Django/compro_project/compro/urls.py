# compro/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_proveedor/', views.add_proveedor, name='add_proveedor'),
    path('list_proveedores/', views.list_proveedores, name='list_proveedores'),
    path('add_producto/', views.add_producto, name='add_producto'),
    path('list_productos/', views.list_productos, name='list_productos'),
    path('home/', views.index, name='home'),
]