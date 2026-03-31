from django.urls import path
from . import views

#Atribuindo caminho para o html e ligando ao view
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastrar_cliente, name='cadastro_cliente'),
    path('login/', views.login_cliente, name='login'),
    path('encomenda/', views.criar_encomenda, name='criar_encomenda'),
]
