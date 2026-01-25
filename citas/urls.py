from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_citas, name='listar_citas'),
    path('nueva/', views.crear_cita, name='crear_cita'),
    path('cancelar/<int:cita_id>/', views.cancelar_cita, name='cancelar_cita'),
]
