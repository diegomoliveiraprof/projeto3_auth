from django.contrib import admin
from .models import Autor, Livro
from rest_framework.authtoken.models import Token

# Admin para o modelo Autor: mostra o campo 'nome' e permite busca por nome
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
   list_display = ['nome']      # colunas exibidas na listagem
   search_fields = ['nome']     # campos pesquisáveis

# Admin para o modelo Livro: exibe campos principais e adiciona filtros
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
   list_display = ['titulo', 'autor', 'isbn', 'ano', 'paginas']  # colunas na listagem
   search_fields = ['titulo', 'isbn']                            # campos pesquisáveis
   list_filter = ['ano', 'autor']                                # filtros laterais

admin.site.register(Token)
