from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='principal/', view=include('principal.urls')),
    path(route='candidato/', view=include('candidato.urls'))
]
