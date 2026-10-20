# importarLivros.py
import sqlite3
import csv

# Caminho para o banco SQLite
db_path = "db.sqlite3"

# Conecta ao banco
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Abre o CSV e insere os dados
with open("base_livros.csv", newline="", encoding="utf-8") as csvfile:
   arquivo = csv.DictReader(csvfile)
   for linha in arquivo:
       nome_autor = linha["autor"].strip()

       # Verifica se o autor já existe
       cursor.execute("SELECT id FROM livros_autor WHERE nome = ?", (nome_autor,))
       resultado = cursor.fetchone()

       if resultado:
           autor_id = resultado[0]  # reutiliza o autor existente
       else:
           cursor.execute("INSERT INTO livros_autor (nome) VALUES (?)", (nome_autor,))
           autor_id = cursor.lastrowid  # cria novo autor

       # Insere livro
       cursor.execute("""
           INSERT INTO livros_livro (titulo, autor_id, isbn, paginas, ano)
           VALUES (?, ?, ?, ?, ?)
       """, (
           linha["titulo"].strip(), autor_id, linha["isbn"].strip(),
           int(linha["paginas"]) if linha["paginas"].isdigit() else None,
           int(linha["ano"]) if linha["ano"].isdigit() else None
       ))

# Salva e fecha
conn.commit()
conn.close()

print("Importação concluída com sucesso!")