## Autores
Desenvolvido por: 
- David Rodrigues Costa
- Pedro Henrique Guedes
- Pedro Igor Ferreira de Carvalho
- Karlos
  
## Descrição
Este projeto consiste no desenvolvimento de um sistema web para gestão de uma doceria, com foco no controle de clientes, produtos e encomendas.
O sistema foi desenvolvido utilizando o framework Django, com o objetivo de aplicar conceitos de programação, organização de código e integração entre diferentes componentes.


## Objetivo
Criar um sistema funcional baseado no MVP que permita:

- Cadastro de clientes
- Login de usuários
- Cadastro e gerenciamento de produtos
- Realização de encomendas
- Organização de pedidos por cliente


## Tecnologias Utilizadas

- Python
- Django
- SQLite
- HTML (básico)

## Estrutura do Sistema

O sistema é dividido em:

- **Models:** Estrutura do banco de dados
- **Views:** Lógica do sistema
- **Forms:** Manipulação de formulários
- **Templates:** Interface (HTML)

## Tipos de Usuário

- **Cliente**
  - Pode se cadastrar
  - Pode realizar encomendas

- **Operador**
  - Criado pelo administrador
  - Pode cadastrar produtos
  - Pode realizar encomendas

- **Administrador**
  - Controle total do sistema
  - Gerencia operadores

## Funcionalidades Implementadas

- Cadastro de cliente com vínculo ao usuário do sistema
- Sistema de login utilizando autenticação do Django
- Cadastro de produtos (pronta entrega e encomenda)
- Criação de encomendas com:
  - Cliente
  - Operador (opcional)
  - Data de retirada
  - Observações
- Associação de múltiplos produtos a uma encomenda
- Controle de status da encomenda

## Testes

As funcionalidades foram testadas utilizando o **shell do Django** e a **página admin**, validando:

- Criação de usuários
- Criação de clientes
- Cadastro de produtos
- Criação de encomendas
- Associação entre entidades

## Como Executar o Projeto

1. Clonar o repositório:
bash
git clone <link-do-repositorio>

2. Acessar a pasta:
cd doceria

3. Instalar dependências:
pip install django

5. Aplicar migrações:
python manage.py migrate

6. Executar:
python manage.py createsuperuser

7. Rodar o servidor:
python manage.py runserver

8. Acessar no navegador:
http://127.0.0.1:8000/

Essa vai ser a página inicial, outras páginas:
http://127.0.0.1:8000/admin
http://127.0.0.1:8000/cadastro_cliente
http://127.0.0.1:8000/login
http://127.0.0.1:8000/criar_encomenda

> Observação: As páginas ainda não possuem estilização completa e nem estão tão úteis; o foco deste primeiro envio foi implementar as funcionalidades principais, testar via terminal ou via admin(melhor).

## Teste via Terminal (Django Shell)

Para validar o funcionamento do sistema:

1. Abrir o shell:
python manage.py shell

2. Criar usuário:
from django.contrib.auth.models import User
user = User.objects.create_user(username="sla", email="sla@gmail.com", password="123")

3. Criar cliente:
from core.models import Cliente
cliente = Cliente.objects.create(user=user, nome="Pedro", telefone="999999999", endereco="Rua A", email="teste@gmail.com")

4. Criar produto:
from core.models import Produto
produto = Produto.objects.create(nome="Bolo", descricao="Chocolate", valor=50.00, quantidade=10, tipo="encomenda")

5. Criar encomenda:
from core.models import Encomenda
from datetime import date
encomenda = Encomenda.objects.create(cliente=cliente, data_retirada=date.today())

6. Adicionar item:
from core.models import ItensEncomenda
ItensEncomenda.objects.create(encomenda=encomenda, produto=produto, quantidade=2)

7. Ver resultados:
Encomenda.objects.all()
