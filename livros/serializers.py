from rest_framework import serializers  # ferramentas do DRF transformar a tabela em JSON
from .models import Autor, Livro        # modelos usados pelos serializers

class AutorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Autor
       fields = '__all__'  # expõe todos os campos do modelo Autor

class LivroSerializer(serializers.ModelSerializer):
   class Meta:
       model = Livro
       fields = '__all__'  # expõe todos os campos do modelo Livro
