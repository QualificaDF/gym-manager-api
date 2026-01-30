
import sqlite3

def get_connection():
    return sqlite3.connect("database.db")

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS planos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        valor_mensal REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        peso REAL NOT NULL,
        altura REAL NOT NULL,
        plano_id INTEGER,
        FOREIGN KEY (plano_id) REFERENCES planos(id)
    )
    """)

    conn.commit()
    conn.close()
