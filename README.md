# API de Livros

API REST para consultar e gerenciar livros e autores, desenvolvida com Django e Django REST Framework com Django-Filter para filtros de pesquisa. Os dados são armazenados em um banco SQLite.

**Nesta versão do projeto foi adicionada autenticação por sessão e token.**

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

## Rotas da API

O Django REST Framework disponibiliza a interface navegável da API no navegador.

| Recurso | Rota | Operações |
| --- | --- | --- |
| Autores | `/api/autores/` | Listar (`GET`) e criar (`POST`) |
| Autor específico | `/api/autores/{id}/` | Consultar (`GET`), atualizar (`PUT`/`PATCH`) e excluir (`DELETE`) |
| Livros | `/api/livros/` | Listar (`GET`) e criar (`POST`) |
| Livro específico | `/api/livros/{id}/` | Consultar (`GET`), atualizar (`PUT`/`PATCH`) e excluir (`DELETE`) |
| Obter token | `/api/token/` | Obter token (`POST`) |
| Administração Django | `/admin/` | Painel administrativo |

Substitua `{id}` pelo identificador do autor ou livro. As rotas de autores e livros oferecem operações CRUD. A listagem de livros aceita filtros por título, nome do autor, ISBN e ano, por exemplo:

```text
http://127.0.0.1:8000/api/livros/?titulo=Dom%20Casmurro
http://127.0.0.1:8000/api/livros/?autor__nome=Machado%20de%20Assis
http://127.0.0.1:8000/api/livros/?ano=1899
```

## Autenticação e permissões

As consultas (`GET`, `HEAD` e `OPTIONS`) são públicas. Para criar, atualizar ou excluir registros (`POST`, `PUT`, `PATCH` e `DELETE`), é necessário estar autenticado. A API aceita autenticação por token e por sessão do Django.

### Autenticação por token

Crie um usuário, caso ainda não tenha um:

```bash
python manage.py createsuperuser
```

Envie um `POST` para `http://127.0.0.1:8000/api/token/` com os campos `username` e `password` no corpo da requisição. A chamada pode ser feita pela interface navegável da API ou por um cliente HTTP.

A resposta contém o token:

```json
{"token": "seu-token"}
```

Inclua esse valor no cabeçalho `Authorization` das requisições que alteram dados:

```bash
curl -X POST http://127.0.0.1:8000/api/livros/ \
  -H "Authorization: Token seu-token" \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Novo livro", "autor": 1, "isbn": "1234567890", "paginas": 200, "ano": 2026}'
```

No Prompt de Comando do Windows (CMD), use `^` para continuar o comando na linha seguinte:

```cmd
curl -X POST http://127.0.0.1:8000/api/livros/ ^
  -H "Authorization: Token seu-token" ^
  -H "Content-Type: application/json" ^
  -d "{\"titulo\": \"Novo livro\", \"autor\": 1, \"isbn\": \"1234567890\", \"paginas\": 200, \"ano\": 2026}"
```

Substitua os dados do exemplo pelos campos e valores válidos para o recurso. Mantenha o token em segredo: ele autentica as requisições como o usuário associado.

### Autenticação por sessão

A autenticação por sessão usa a sessão autenticada do Django no navegador. Por exemplo, um usuário autenticado no painel `/admin/` pode usar a mesma sessão na interface navegável da API. Nas requisições que alteram dados, o Django também exige a proteção CSRF; prefira o formulário da interface navegável ou envie o cookie e o token CSRF correspondentes.
