import sqlite3

def conectar():
    return sqlite3.connect("sabor_express.db")

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            ativo INTEGER NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()