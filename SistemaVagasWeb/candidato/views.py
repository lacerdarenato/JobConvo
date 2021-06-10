from django.shortcuts import render
from . import forms, models


def cadastro(request):
    form = forms.cadastroForm()
    if request.method == 'POST':
        form = forms.cadastroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("Formulário Inválido")
    candidatos_list = models.candidato.objects.order_by('nome')
    data_dict = {
        'form': form,
        'candidatos_list': candidatos_list
    }
    return render(request, 'candidato/cadastro.html', data_dict)
