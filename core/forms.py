from django import forms
from django.contrib.auth.models import User
from .models import Cliente, Encomenda

# FORMULÁRIO DE CADASTRO DE CLIENTE
class CadastroClienteForm(forms.ModelForm):

    # Campo extra (não está no model Cliente)
    # widget=PasswordInput = faz o campo virar senha (******)
    senha = forms.CharField(widget=forms.PasswordInput)

    # Criando campo de email separado (melhor prática)
    email = forms.EmailField()

    class Meta:
        model = Cliente

        # ⚠️ NÃO usamos 'user' aqui diretamente
        # porque vamos criar o User manualmente no save()
        fields = ['nome', 'telefone', 'endereco']

    def save(self, commit=True):
        # commit=False = cria o objeto mas não salva ainda no banco
        cliente = super().save(commit=False)

        # Criação do usuário do Django (login)
        user = User.objects.create_user(
            username=self.cleaned_data['email'],  # usamos email como username
            email=self.cleaned_data['email'],
            password=self.cleaned_data['senha']
        )

        # Ligando cliente ao usuário
        cliente.user = user
        cliente.email = self.cleaned_data['email']

        # Salva no banco
        if commit:
            cliente.save()

        return cliente

# FORMULÁRIO DE LOGIN
class LoginForm(forms.Form):

    # Form simples (não ligado a model)
    email = forms.EmailField()

    # Campo de senha com input escondido
    senha = forms.CharField(widget=forms.PasswordInput)

# FORMULÁRIO DE ENCOMENDA
class EncomendaForm(forms.ModelForm):

    class Meta:
        model = Encomenda

        # Só os campos que o usuário vai preencher
        fields = ['data_retirada', 'observacoes']