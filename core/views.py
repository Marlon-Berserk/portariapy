# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculo, Pedestre, EntradaSaidaVeiculo, EntradaSaidaPedestre, RegistroEntradaSaidaVeiculo
from .forms import VeiculoForm, PedestreForm, EntradaVeiculoForm, SaidaVeiculoForm, EntradaPedestreForm, SaidaPedestreForm
from django.utils import timezone
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def cadastrar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controle_entrada_saida_veiculo')
    else:
        form = VeiculoForm()
    return render(request, 'core/cadastrar_veiculo.html', {'form': form})

def cadastrar_pedestre(request):
    if request.method == 'POST':
        form = PedestreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controle_entrada_saida_pedestre')
    else:
        form = PedestreForm()
    return render(request, 'core/cadastrar_pedestre.html', {'form': form})

def controle_entrada_saida_veiculo(request):
    # Inicializa o formulário de entrada
    form = EntradaVeiculoForm()

    if request.method == 'POST':
        if 'entrada' in request.POST:
            form = EntradaVeiculoForm(request.POST)
            if form.is_valid():
                form.save()  # Salva a entrada do veículo
                # Limpa o formulário após salvar
                form = EntradaVeiculoForm()
        elif 'saida' in request.POST:
            veiculo_id = request.POST.get('veiculo_id')
            if veiculo_id:
                try:
                    # Busca o registro de saída com base no veículo selecionado
                    registro = get_object_or_404(EntradaSaidaVeiculo, id=veiculo_id, hora_saida__isnull=True)
                    registro.hora_saida = timezone.now()
                    registro.save()
                except EntradaSaidaVeiculo.DoesNotExist:
                    return HttpResponse("Registro de saída não encontrado ou já registrado.", status=404)
                
                # Limpa o formulário após registrar a saída
                form = EntradaVeiculoForm()

    veiculos = EntradaSaidaVeiculo.objects.filter(hora_saida__isnull=True)
    return render(request, 'core/controle_entrada_saida_veiculo.html', {'form': form, 'veiculos': veiculos})

def controle_entrada_saida_pedestre(request):
    if request.method == 'POST':
        if 'entrada' in request.POST:
            form = EntradaPedestreForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'saida' in request.POST:
            entrada_pedestre = get_object_or_404(EntradaSaidaPedestre, pk=request.POST.get('pedestre_id'))
            entrada_pedestre.hora_saida = timezone.now()
            entrada_pedestre.save()
    pedestres = EntradaSaidaPedestre.objects.filter(hora_saida__isnull=True)
    form_entrada = EntradaPedestreForm()
    return render(request, 'core/controle_entrada_saida_pedestre.html', {'form_entrada': form_entrada, 'pedestres': pedestres})

def historico_veiculo(request):
    registros = EntradaSaidaVeiculo.objects.all().order_by('-hora_entrada')
    return render(request, 'core/historico_veiculo.html', {'registros': registros})

def historico_pedestre(request):
    registros = EntradaSaidaPedestre.objects.all().order_by('-hora_entrada')
    return render(request, 'core/historico_pedestre.html', {'registros': registros})