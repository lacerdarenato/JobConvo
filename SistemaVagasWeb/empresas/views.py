from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import EmpresaForm
from .models import empresa

def newEmpresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.user = request.user
            empresa.save()
            messages.info(request, 'Empresa criada com sucesso!')
            return redirect('/empresas')
    else:
        form = EmpresaForm()
        return render(request, 'empresas/newempresa.html', {'form': form})

def showEmpresa(request):

    empresaItem = empresa.objects.all().order_by('title')
    return render(request, 'empresas/empresa.html', {'empresa': empresaItem})
