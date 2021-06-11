from django.shortcuts import render, get_object_or_404

from .models import vaga


def vagasList(request):
    vagas = vaga.objects.all()
    return render(request, 'vagas/list.html', {'vagas': vagas})


def vagaView(request, id):
    vagaItem = get_object_or_404(vaga, pk=id)
    return render(request, 'vagas/vaga.html', {'vaga': vagaItem})
