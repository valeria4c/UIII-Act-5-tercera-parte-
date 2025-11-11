from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_spa, name='inicio_spa'),

    # --- Usuarios ---
    path('usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/actualizar/<int:id_usuario>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/borrar/<int:id_usuario>/', views.borrar_usuario, name='borrar_usuario'),

    # --- Pedidos ---
    path('pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('pedidos/agregar/', views.agregar_pedidos, name='agregar_pedidos'),
    path('pedidos/actualizar/<int:id_pedido>/', views.actualizar_pedidos, name='actualizar_pedidos'),
    path('pedidos/borrar/<int:id_pedido>/', views.borrar_pedidos, name='borrar_pedidos'),

    path('reseñas/agregar/', views.agregar_reseñas, name='agregar_reseñas'),
    path('reseñas/ver/', views.ver_reseñas, name='ver_reseñas'),
    path('reseñas/actualizar/<int:id_reseña>/', views.actualizar_reseñas, name='actualizar_reseñas'),
    path('reseñas/borrar/<int:id_reseña>/', views.borrar_reseñas, name='borrar_reseñas'),
]
