from django.contrib import admin
from .models import Cliente, Produto, Encomenda

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Encomenda)