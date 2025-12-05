from django import forms
from .models import Candidato

class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'email', 'telefone', 'curriculo']
