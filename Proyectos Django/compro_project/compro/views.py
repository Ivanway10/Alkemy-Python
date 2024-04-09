from django.http import HttpResponse
from django.shortcuts import render, redirect
from.forms import ProveedorForm, ProductoForm
from.models import Producto, Proveedor


def add_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'compro/add_proveedor.html', {'form': form})

def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_productos')
    else:
        form = ProductoForm()
    return render(request, 'compro/add_producto.html', {'form': form})


def list_productos(request):
    productos = Producto.objects.all()
    return render(request, 'compro/list_productos.html', {'productos': productos})

def index(request):
    return render(request, 'compro/home.html')


def list_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'compro/list_proveedores.html', {'proveedores': proveedores})
