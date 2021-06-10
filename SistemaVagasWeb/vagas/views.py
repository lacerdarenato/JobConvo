from django.shortcuts import render

def vagasList(request):
    return render(request, 'vagas/list.html')
