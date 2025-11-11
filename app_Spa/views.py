from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuarios, Pedidos, Reseñas  # Importamos todos los modelos

# ---------------------------
# Página principal del SPA
# ---------------------------
def inicio_spa(request):
    return render(request, 'inicio.html')


# ---------------------------
# SECCIÓN: USUARIOS
# ---------------------------
def agregar_usuario(request):
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre_completo')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        if Usuarios.objects.filter(correo=correo).exists():
            return render(request, 'usuarios/agregar_usuario.html', {'error': 'Este correo ya está registrado.'})

        Usuarios.objects.create(
            nombre_completo=nombre_completo,
            correo=correo,
            telefono=telefono,
            direccion=direccion
        )
        return redirect('ver_usuarios')
    return render(request, 'usuarios/agregar_usuario.html')


def ver_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios/ver_usuarios.html', {'usuarios': usuarios})


def actualizar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuarios, pk=id_usuario)
    if request.method == 'POST':
        usuario.nombre_completo = request.POST.get('nombre_completo')
        usuario.correo = request.POST.get('correo')
        usuario.telefono = request.POST.get('telefono')
        usuario.direccion = request.POST.get('direccion')
        usuario.activo = 'activo' in request.POST
        usuario.save()
        return redirect('ver_usuarios')
    return render(request, 'usuarios/actualizar_usuario.html', {'usuario': usuario})


def borrar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuarios, pk=id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('ver_usuarios')
    return render(request, 'usuarios/borrar_usuario.html', {'usuario': usuario})


# ---------------------------
# SECCIÓN: PEDIDOS
# ---------------------------
def agregar_pedidos(request):
    usuarios = Usuarios.objects.all() # Necesitamos los usuarios para el ForeignKey
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario')
        servicio = request.POST.get('servicio')
        precio_total = request.POST.get('precio_total')
        notas_adicionales = request.POST.get('notas_adicionales')
        estado = request.POST.get('estado')

        usuario = get_object_or_404(Usuarios, pk=usuario_id)

        pedido = Pedidos.objects.create(
            usuario=usuario,
            servicio=servicio,
            precio_total=precio_total,
            notas_adicionales=notas_adicionales,
            estado=estado
        )
        return redirect('ver_pedidos')
    return render(request, 'pedidos/agregar_pedidos.html', {'usuarios': usuarios})

def ver_pedidos(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'pedidos/ver_pedidos.html', {'pedidos': pedidos})

def actualizar_pedidos(request, id_pedido):
    pedido = get_object_or_404(Pedidos, pk=id_pedido)
    usuarios = Usuarios.objects.all() # Necesitamos los usuarios para el ForeignKey
    if request.method == 'POST':
        pedido.usuario = get_object_or_404(Usuarios, pk=request.POST.get('usuario'))
        pedido.servicio = request.POST.get('servicio')
        pedido.precio_total = request.POST.get('precio_total')
        pedido.notas_adicionales = request.POST.get('notas_adicionales')
        pedido.estado = request.POST.get('estado')
        pedido.save()
        return redirect('ver_pedidos')
    return render(request, 'pedidos/actualizar_pedidos.html', {'pedido': pedido, 'usuarios': usuarios})

def borrar_pedidos(request, id_pedido):
    pedido = get_object_or_404(Pedidos, pk=id_pedido)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'pedidos/borrar_pedidos.html', {'pedido': pedido})


# ---------------------------
# SECCIÓN: RESEÑAS
# ---------------------------
# Funciones CRUD para Reseñas

def agregar_reseñas(request):
    usuarios = Usuarios.objects.all()
    pedidos = Pedidos.objects.all()
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario')
        pedido_id = request.POST.get('pedido')
        titulo = request.POST.get('titulo')
        comentario = request.POST.get('comentario')
        calificacion = request.POST.get('calificacion')
        visible = 'visible' in request.POST

        usuario = get_object_or_404(Usuarios, pk=usuario_id)
        pedido = get_object_or_404(Pedidos, pk=pedido_id)

        reseña = Reseñas.objects.create(
            usuario=usuario,
            pedido=pedido,
            titulo=titulo,
            comentario=comentario,
            calificacion=calificacion,
            visible=visible
        )
        return redirect('ver_reseñas')
    return render(request, 'reseñas/agregar_reseñas.html', {'usuarios': usuarios, 'pedidos': pedidos})

def ver_reseñas(request):
    reseñas = Reseñas.objects.all()
    return render(request, 'reseñas/ver_reseñas.html', {'reseñas': reseñas})

def actualizar_reseñas(request, id_reseña):
    reseña = get_object_or_404(Reseñas, pk=id_reseña)
    usuarios = Usuarios.objects.all()
    pedidos = Pedidos.objects.all()
    if request.method == 'POST':
        reseña.usuario = get_object_or_404(Usuarios, pk=request.POST.get('usuario'))
        reseña.pedido = get_object_or_404(Pedidos, pk=request.POST.get('pedido'))
        reseña.titulo = request.POST.get('titulo')
        reseña.comentario = request.POST.get('comentario')
        reseña.calificacion = request.POST.get('calificacion')
        reseña.visible = 'visible' in request.POST
        reseña.save()
        return redirect('ver_reseñas')
    return render(request, 'reseñas/actualizar_reseñas.html', {'reseña': reseña, 'usuarios': usuarios, 'pedidos': pedidos})

def borrar_reseñas(request, id_reseña):
    reseña = get_object_or_404(Reseñas, pk=id_reseña)
    if request.method == 'POST':
        reseña.delete()
        return redirect('ver_reseñas')
    return render(request, 'reseñas/borrar_reseñas.html', {'reseña': reseña})
