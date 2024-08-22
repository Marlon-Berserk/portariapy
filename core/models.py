# core/models.py

from django.db import models
from django.utils import timezone

class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=20, unique=True)
    cor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.placa}"

class Pedestre(models.Model):
    nome_completo = models.CharField(max_length=150)
    documento_identificacao = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome_completo

class EntradaSaidaVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    hora_entrada = models.DateTimeField(default=timezone.now)
    hora_saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.veiculo} - Entrada: {self.hora_entrada} Saída: {self.hora_saida or 'Ainda no local'}"

class EntradaSaidaPedestre(models.Model):
    pedestre = models.ForeignKey(Pedestre, on_delete=models.CASCADE)
    hora_entrada = models.DateTimeField(default=timezone.now)
    hora_saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.pedestre} - Entrada: {self.hora_entrada} Saída: {self.hora_saida or 'Ainda no local'}"

class RegistroEntradaSaidaVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    horario_entrada = models.DateTimeField(default=timezone.now)
    horario_saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.veiculo} - Entrada: {self.horario_entrada} - Saída: {self.horario_saida}'