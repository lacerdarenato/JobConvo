from django.urls import path

from . import views

urlpatterns = [
    path('', views.vagasList, name='vagas-list'),
    path('<int:id>', views.vagaView, name='vaga-view'),


]