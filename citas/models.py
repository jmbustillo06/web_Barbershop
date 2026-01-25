from django.db import models
from django.contrib.auth.models import User


class Cita(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    )

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    servicio = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente'
    )
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.username} - {self.fecha} {self.hora}"
