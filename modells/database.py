import sqlite3


def criar_banco():
    conexao = sqlite3.connect('gym_manager.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            plano_id INTEGER NOT NULL,
            FOREIGN KEY (plano_id) REFERENCES planos (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS planos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            valor_mensal REAL NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()
    print("Banco criado e dados inseridos com sucesso!")
