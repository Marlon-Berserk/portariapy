# portaria/urls.py

from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('cadastrar-veiculo/', views.cadastrar_veiculo, name='cadastrar_veiculo'),
    path('cadastrar-pedestre/', views.cadastrar_pedestre, name='cadastrar_pedestre'),
    path('controle-veiculos/', views.controle_entrada_saida_veiculo, name='controle_entrada_saida_veiculo'),
    path('controle-pedestres/', views.controle_entrada_saida_pedestre, name='controle_entrada_saida_pedestre'),
    path('historico-veiculos/', views.historico_veiculo, name='historico_veiculo'),
    path('historico-pedestre/', views.historico_pedestre, name='historico_pedestre'),
]
