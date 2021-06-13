from django.contrib import admin
from django.urls import path, include

from . import views
from vagas import views as viewVagas

urlpatterns = [
    path('', views.showEmpresa, name='show-empresa'),
    path('newempresa/', views.newEmpresa, name='new-empresa'),
    path('newvaga/', viewVagas.newVaga, name='new-vaga'),
    path('editvaga/<int:id>', viewVagas.editVaga, name='edit-vaga'),
    path('deletevaga/<int:id>', viewVagas.deleteVaga, name='delete-vaga'),
]