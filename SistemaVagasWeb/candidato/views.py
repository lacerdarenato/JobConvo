from django.shortcuts import render
from . import forms


def cadastro(request):
    form = forms.cadastroForm()
    data_dict = {'form': form}
    return render(request, 'candidato/cadastro.html', data_dict)
