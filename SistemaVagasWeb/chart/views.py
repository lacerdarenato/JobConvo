import json
from django.shortcuts import render
from django.db.models.functions import ExtractMonth
from django.db.models import Count

from vagas.models import vaga


def relatorioVagas(request):
    queryset = vaga.objects.annotate(month=ExtractMonth('created_at')).values('month').annotate(count=Count('id'))

    labels = [obj[0] for obj in queryset.values_list('month')]
    values = [obj[0] for obj in queryset.values_list('count')]

    context = {
        'names': json.dumps(labels),
        'prices': json.dumps(values),
    }
    return render(request, 'chart/relatorios.html', context)