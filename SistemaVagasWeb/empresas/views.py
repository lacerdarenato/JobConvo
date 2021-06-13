from django.shortcuts import render

from .models import empresa

def showEmpresa(request):

    empresaItem = empresa.objects.order_by('title')
    return render(request, 'empresas/empresa.html', {'empresa': empresaItem})
