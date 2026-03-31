from django.db import models
from django.contrib.auth.models import User


# CLIENTE
class Cliente(models.Model):
    # OneToOneField = relação 1 para 1 com User
    # Cada cliente tem um único usuário e vice-versa
    # CASCADE = se o usuário for deletado, o cliente também será
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    # CharField = texto curto com limite de caracteres
    nome = models.CharField(max_length=100)

    # Telefone como string (não usar número por causa de formatação)
    telefone = models.CharField(max_length=20)

    # Endereço simples
    endereco = models.CharField(max_length=200)

    # Email com validação automática
    email = models.EmailField(blank=True, null=True)

    # Define como o objeto aparece no sistema (admin, shell, etc)
    def __str__(self):
        return self.nome

# OPERADOR
class Operador(models.Model):
    # Também é um usuário, mas com função diferente no sistema
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        # Mostra o username do usuário
        return self.user.username

# PRODUTO
class Produto(models.Model):

    # Choices = limita os valores possíveis do campo "tipo"
    # Primeiro valor é o que vai pro banco
    # Segundo é o que aparece no sistema
    TIPO_PRODUTO = [
        ('pronta_entrega', 'Pronta Entrega'),
        ('encomenda', 'Encomenda')
    ]

    nome = models.CharField(max_length=100)

    # TextField = texto maior (sem limite pequeno)
    descricao = models.TextField()

    # DecimalField = usado para dinheiro
    # max_digits = total de dígitos
    # decimal_places = casas decimais
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    # Só aceita números positivos (melhor que IntegerField)
    quantidade = models.PositiveIntegerField()

    # Campo com opções limitadas (choices)
    tipo = models.CharField(max_length=20, choices=TIPO_PRODUTO)

    def __str__(self):
        return f'{self.nome} - R${self.valor}'

# ENCOMENDA
class Encomenda(models.Model):

    # Status controlado (tipo enum)
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('preparando', 'Preparando'),
        ('pronto', 'Pronto'),
        ('entregue', 'Entregue')
    ]

    # ForeignKey = relação 1 para muitos
    # Um cliente pode ter várias encomendas
    # CASCADE = se cliente for deletado, encomendas também serão
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    # Operador pode ser nulo (pedido pode ser feito pelo cliente)
    # SET_NULL = se operador for deletado, fica como NULL
    operador = models.ForeignKey(
        Operador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # Data que o pedido será retirado
    data_retirada = models.DateField()

    # Data automática de criação do pedido
    auto_now_add = True
    data_criacao = models.DateTimeField(auto_now_add=True)

    # Campo opcional (blank=True permite vazio no formulário)
    observacoes = models.TextField(blank=True)

    # Status com valores limitados
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    # ManyToMany = muitos para muitos
    # Uma encomenda pode ter vários produtos
    # Um produto pode estar em várias encomendas
    # through = usa tabela intermediária (ItensEncomenda)
    produtos = models.ManyToManyField(Produto, through='ItensEncomenda')

    def __str__(self):
        return f'Encomenda #{self.id} - {self.cliente.nome}'

# ITENS DA ENCOMENDA
class ItensEncomenda(models.Model):

    # Cada item pertence a uma encomenda
    # CASCADE = se encomenda for deletada, os itens também serão
    encomenda = models.ForeignKey(Encomenda, on_delete=models.CASCADE)

    # Produto relacionado ao item
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    # Quantidade daquele produto na encomenda
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade}x (Encomenda {self.encomenda.id})'