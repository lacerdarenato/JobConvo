from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

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
            messages.info(request, 'Vaga criada com sucesso!')
            return redirect('/vagas')
        else:
            print("Formulário Inválido")
    form = VagaForm()
    return render(request, 'vagas/addvaga.html', {'form': form})

def editVaga(request, id):
    vagaItem = get_object_or_404(vaga, pk=id)
    form = VagaForm(instance=vagaItem)

    if(request.method == 'POST'):
        form = VagaForm(request.POST, instance=vagaItem)
        if(form.is_valid()):
            vagaItem.save()

            messages.info(request, 'Vaga editada com sucesso!')
            return redirect('/vagas')
        else:
            return render(request, 'vagas/editvaga.html', {'form': form, 'vaga': vagaItem})
    else:
        return render(request, 'vagas/editvaga.html', {'form': form, 'vaga': vagaItem})

def deleteVaga(request, id):
    vagaItem = get_object_or_404(vaga, pk=id)
    vagaItem.delete()

    messages.info(request, 'Vaga deletada com sucesso!')
    return redirect('/vagas')