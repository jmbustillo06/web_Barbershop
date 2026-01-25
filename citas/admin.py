from django.contrib import admin
from .models import Cita


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'hora', 'servicio', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente__username', 'servicio')
