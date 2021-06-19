from django.urls import path

from . import views

urlpatterns = [
    path('', views.vagasList, name='vagas-list'),
    path('<int:id>/', views.vagaView, name='vaga-view'),
    path('newvaga/', views.newVaga, name='new-vaga'),
    path('editvaga/<int:id>', views.editVaga, name='edit-vaga'),
    path('deletevaga/<int:id>', views.deleteVaga, name='delete-vaga'),
    path('candidatar/<int:id>', views.candidatar_vaga, name='candidatar-vaga'),

]