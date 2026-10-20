from rest_framework import viewsets                       # viewsets do DRF para CRUD automático
from .models import Autor, Livro                          # modelos/tabelas usados nas views
from .serializers import AutorSerializer, LivroSerializer # serializers para (de)serializar os modelos
from django_filters.rest_framework import DjangoFilterBackend  # permite filtragem via query params

# ViewSet para o modelo Autor — fornece endpoints list/retrieve/create/update/destroy
class AutorViewSet(viewsets.ModelViewSet):
   queryset = Autor.objects.all()         # queryset base usado pelo ViewSet
   serializer_class = AutorSerializer     # serializer que define representação e validação

# ViewSet para o modelo Livro — fornece endpoints CRUD e suporte a filtros
class LivroViewSet(viewsets.ModelViewSet):
   queryset = Livro.objects.all()         # queryset base para operações do ViewSet
   serializer_class = LivroSerializer     # serializer usado para livros
   filter_backends = [DjangoFilterBackend]  # habilita filtragem via django-filter
   # campos permitidos para filtragem via query string, ex: ?titulo=foo or ?autor__nome=Silva
   filterset_fields = ['titulo', 'autor__nome', 'isbn', 'ano']
