from django.contrib import admin          # painel administrativo do Django
from django.urls import path, include     # path para rotas, include para incluir outras URLs
from rest_framework.routers import DefaultRouter  # router que gera rotas para ViewSets
from livros.views import AutorViewSet, LivroViewSet  # ViewSets registrados no router

router = DefaultRouter()
router.register(r'autores', AutorViewSet)  # registra endpoints para autores: /api/autores/
router.register(r'livros', LivroViewSet)   # registra endpoints para livros: /api/livros/

urlpatterns = [
   path('admin/', admin.site.urls),           # rota do Django admin
   path('api/', include(router.urls)),        # inclui rotas geradas pelo router sob o prefixo /api/
]
