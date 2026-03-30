from django.shortcuts import render

def index(request):
    return render(request, 'core/site.html')

from django.shortcuts import render, redirect
from .models import Cliente

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')

        Cliente.objects.create(
            nome=nome,
            telefone=telefone,
            email=email,
            endereco=endereco
        )

        return redirect('/')

    return render(request, 'core/cadastro_cliente.html')