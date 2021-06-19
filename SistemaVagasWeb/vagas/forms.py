from django import forms

from .models import vaga, Candidatura


class VagaForm(forms.ModelForm):

    class Meta:
        model = vaga
        fields = ('title', 'requirements', 'salaryRange', 'minimalEducationLevel')


class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = ('vaga', 'cand')
