# app_Spa/models.py
from django.db import models

# ==========================================
# MODELO: USUARIOS
# ==========================================
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    correo = models.EmailField(unique=True, max_length=250)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_completo


# ==========================================
# MODELO: PEDIDOS
# ==========================================
class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.CASCADE,
        related_name="pedidos"
    )
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    servicio = models.CharField(max_length=100)
    precio_total = models.DecimalField(max_digits=8, decimal_places=2)
    notas_adicionales = models.TextField(blank=True, null=True)
    estado = models.CharField(
        max_length=50,
        default="pendiente",
        choices=[
            ("pendiente", "Pendiente"),
            ("en_proceso", "En Proceso"),
            ("completado", "Completado"),
            ("cancelado", "Cancelado"),
        ]
    )

    def __str__(self):
        return f"Pedido #{self.id_pedido} - {self.servicio}"


# ==========================================
# MODELO: RESEÑAS
# ==========================================
class Reseñas(models.Model):
    id_reseña = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.CASCADE,
        related_name="reseñas"
    )
    pedido = models.ForeignKey(
        Pedidos,
        on_delete=models.CASCADE,
        related_name="reseñas"
    )
    titulo = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.IntegerField(default=5)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.calificacion}⭐"
