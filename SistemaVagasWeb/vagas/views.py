from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import VagaForm
from .models import vaga

@login_required
def vagasList(request):

    search = request.GET.get('search')
    if search:
        vagas = vaga.objects.filter(title__icontains=search)
    else:
        vagaslist = vaga.objects.all().order_by('-created_at')
        paginator = Paginator(vagaslist, 5)
        page = request.GET.get('page')
        vagas = paginator.get_page(page)
    return render(request, 'vagas/list.html', {'vagas': vagas})

@login_required
def vagaView(request, id):
    vagaItem = get_object_or_404(vaga, pk=id)
    form = VagaForm(request.GET, instance=vagaItem)
    return render(request, 'vagas/vaga.html', {'form': form, 'vaga': vagaItem})
@login_required
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
@login_required
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
@login_required
def deleteVaga(request, id):
    vagaItem = get_object_or_404(vaga, pk=id)
    vagaItem.delete()

    messages.info(request, 'Vaga deletada com sucesso!')
    return redirect('/vagas')