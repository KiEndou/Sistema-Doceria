from django.contrib import admin
from .models import Cliente, Produto, Encomenda, Operador, ItensEncomenda

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Encomenda)
admin.site.register(Operador)
admin.site.register(ItensEncomenda)