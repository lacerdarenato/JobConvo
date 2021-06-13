from django import forms
from candidato.models import candidato


class cadastroForm(forms.ModelForm):

    class Meta:
        model = candidato
        fields = '__all__'