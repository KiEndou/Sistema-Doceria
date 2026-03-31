from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from .forms import CadastroClienteForm, LoginForm
from .models import Produto, Encomenda, Cliente, Operador

# PÁGINA INICIAL / CATÁLOGO
def index(request):
    # Busca todos os produtos do banco
    produtos = Produto.objects.all()

    # Envia os produtos para o HTML
    return render(request, 'core/index.html', {'produtos': produtos})

# CADASTRO DE CLIENTE
def cadastrar_cliente(request):

    # Se o usuário enviou o formulário
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)

        # Verifica se os dados são válidos
        if form.is_valid():
            form.save()  # Salva cliente + cria usuário

            # Redireciona para login
            return redirect('login')

    else:
        # Se for GET (abrir página)
        form = CadastroClienteForm()

    return render(request, 'core/cadastro_cliente.html', {'form': form})

# LOGIN
def login_cliente(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            # Tenta encontrar o usuário pelo email
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            # Se encontrou o usuário
            if user:
                # Autentica usando username (Django usa username internamente)
                auth_user = authenticate(
                    request,
                    username=user.username,
                    password=senha
                )

                if auth_user:
                    # Faz login (cria sessão)
                    login(request, auth_user)

                    # 🔥 REDIRECIONAMENTO POR TIPO DE USUÁRIO
                    if auth_user.is_superuser:
                        return redirect('painel_admin')

                    elif Operador.objects.filter(user=auth_user).exists():
                        return redirect('painel_operador')

                    elif Cliente.objects.filter(user=auth_user).exists():
                        return redirect('painel_cliente')

                    # fallback
                    return redirect('index')
                return render(request, 'core/login.html', {'form': form})

    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Produto, Encomenda, ItensEncomenda, Cliente
from datetime import date

def criar_encomenda(request):
    produtos = Produto.objects.all()

    if request.method == 'POST':
        cliente = Cliente.objects.get(user=request.user)

        data_retirada = request.POST.get('data_retirada')
        observacoes = request.POST.get('observacoes')

        encomenda = Encomenda.objects.create(
            cliente=cliente,
            data_retirada=data_retirada,
            observacoes=observacoes
        )

        # pegar produtos e quantidades
        for produto in produtos:
            quantidade = request.POST.get(f'produto_{produto.id}')

            if quantidade and int(quantidade) > 0:
                ItensEncomenda.objects.create(
                    encomenda=encomenda,
                    produto=produto,
                    quantidade=int(quantidade)
                )

        return redirect('index')

    return render(request, 'core/criar_encomenda.html', {'produtos': produtos})