from django.shortcuts import render, get_object_or_404, redirect

from .forms import VagaForm
from .models import vaga


def vagasList(request):
    vagas = vaga.objects.all().order_by('-created_at')
    return render(request, 'vagas/list.html', {'vagas': vagas})


def vagaView(request, id):
    vagaItem = get_object_or_404(vaga, pk=id)
    return render(request, 'vagas/vaga.html', {'vaga': vagaItem})

def newVaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/vagas')
        else:
            print("Formulário Inválido")
    form = VagaForm()
    return render(request, 'vagas/addvaga.html', {'form': form})