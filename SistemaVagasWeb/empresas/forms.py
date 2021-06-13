from django import forms

from .models import empresa


class EmpresaForm(forms.ModelForm):

    class Meta:
        model = empresa
        fields = 'title'
