# API de Livros

API REST para consultar e gerenciar livros e autores, desenvolvida com Django e Django REST Framework com Django-Filter para filtros de pesquisa. Os dados são armazenados em um banco SQLite.

**Nesta versão da atividade projeto3 foi adicionada a atutenticação via sessão e token**

## Requisitos

- Python 3.12 ou superior
- Git

## Clonar e iniciar

No PowerShell, execute:

```powershell
git clone https://github.com/diegomoliveiraprof/projeto3.git
cd projeto3

python -m venv venv
.\venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Se o PowerShell bloquear a ativação do ambiente virtual, consulte a [documentação de políticas de execução do PowerShell](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_execution_policies) ou use o Command Prompt - CMD:

No CMD, execute:

```powershell
git clone https://github.com/diegomoliveiraprof/projeto3.git
cd projeto3

python -m venv venv
venv\Scripts\activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

O servidor estará disponível em <http://127.0.0.1:8000/>.

### Linux ou macOS

```bash
git clone https://github.com/diegomoliveiraprof/projeto3.git
cd projeto3

python3 -m venv venv
source venv/bin/activate

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
O servidor estará disponível em <http://127.0.0.1:8000/>. 

## Dados iniciais (opcional)

O banco `db.sqlite3` não é versionado. O comando `migrate` cria um banco local vazio. Para preenchê-lo com os registros de `base_livros.csv`, execute na raiz do projeto:

PowerShell / CMD (Windows) ou CLI/Terminal (Linux, macOS)
```bash
python importarDados.py
```

Execute a importação apenas uma vez por banco: o script insere os registros do CSV e não verifica se os livros já foram importados. Pode gerar duplicação de dados.

## Endpoints

O Django REST Framework disponibiliza a interface navegável da API no navegador:

| Recurso | Endpoint |
| --- | --- |
| Autores | `http://127.0.0.1:8000/api/autores/` |
| Livros | `http://127.0.0.1:8000/api/livros/` |
| Administração Django | `http://127.0.0.1:8000/admin/` |

Os endpoints de autores e livros oferecem operações CRUD. A listagem de livros aceita filtros por título, nome do autor, ISBN e ano, por exemplo:

```text
http://127.0.0.1:8000/api/livros/?titulo=Dom%20Casmurro
http://127.0.0.1:8000/api/livros/?autor__nome=Machado%20de%20Assis
http://127.0.0.1:8000/api/livros/?ano=1899
```
