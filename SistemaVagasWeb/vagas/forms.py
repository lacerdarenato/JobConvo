from django import forms

from .models import vaga


class VagaForm(forms.ModelForm):

    class Meta:
        model = vaga
        fields = ('title', 'requirements', 'salaryRange', 'minimalEducationLevel')