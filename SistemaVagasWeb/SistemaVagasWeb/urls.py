from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='', view=include('principal.urls')),
    path(route='principal/', view=include('principal.urls')),
    path(route='candidato/', view=include('candidato.urls')),
    path(route='vagas/', view=include('vagas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
