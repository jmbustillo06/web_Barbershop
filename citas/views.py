from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cita
from .forms import CitaForm


@login_required
def listar_citas(request):
    citas = Cita.objects.filter(cliente=request.user).order_by('-fecha')
    return render(request, 'citas/listar.html', {'citas': citas})


@login_required
def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.cliente = request.user
            cita.save()
            return redirect('listar_citas')
    else:
        form = CitaForm()

    return render(request, 'citas/crear.html', {'form': form})


@login_required
def cancelar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, cliente=request.user)
    cita.estado = 'cancelada'
    cita.save()
    return redirect('listar_citas')
