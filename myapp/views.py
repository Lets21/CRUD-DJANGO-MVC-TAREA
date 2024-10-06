from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Producto
from .forms import ProductoForm

def inicio(request):
    return render(request, 'inicio.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al login después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user  # Asignar el usuario actual
            producto.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

@login_required
def listar_productos(request):
    productos = Producto.objects.filter(usuario=request.user)  # Filtrar por usuario
    return render(request, 'listar_productos.html', {'productos': productos})


@login_required
def editar_producto(request, id):
    producto = Producto.objects.get(id=id, usuario=request.user)  # Verificar que el producto pertenece al usuario
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id, usuario=request.user)  # Verificar que el producto pertenece al usuario
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})
