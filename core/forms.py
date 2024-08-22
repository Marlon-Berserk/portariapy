# core/forms.py

from django import forms
from .models import Veiculo, Pedestre, EntradaSaidaVeiculo, EntradaSaidaPedestre

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['nome', 'modelo', 'placa', 'cor']

class PedestreForm(forms.ModelForm):
    class Meta:
        model = Pedestre
        fields = ['nome_completo', 'documento_identificacao']

class EntradaVeiculoForm(forms.ModelForm):
    class Meta:
        model = EntradaSaidaVeiculo
        fields = ['veiculo']

    def __init__(self, *args, **kwargs):
        super(EntradaVeiculoForm, self).__init__(*args, **kwargs)
        self.fields['veiculo'].queryset = Veiculo.objects.all()

class SaidaVeiculoForm(forms.ModelForm):
    class Meta:
        model = EntradaSaidaVeiculo
        fields = []

class EntradaPedestreForm(forms.ModelForm):
    class Meta:
        model = EntradaSaidaPedestre
        fields = ['pedestre']

class SaidaPedestreForm(forms.ModelForm):
    class Meta:
        model = EntradaSaidaPedestre
        fields = []
