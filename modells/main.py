from database import *
import sqlite3

criar_banco()
conexao = sqlite3.connect('gym_manager.db')
cursor = conexao.cursor()

nome = input("Nome: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

print("\nPlanos: [1] Mensal - R$99,99 | [2] Anual - R$129,99")
opcao = int(input("Qual plano deseja (1 ou 2)? "))

if opcao == 1:
    nome_plano, valor = "Mensal", 99.99
else:
    nome_plano, valor = "Anual", 129.99


cursor.execute("INSERT INTO planos (nome, valor_mensal) VALUES (?, ?)", (nome_plano, valor))
plano_id = cursor.lastrowid

cursor.execute("INSERT INTO alunos (nome, peso, altura, plano_id ) VALUES (?, ?, ?, ?)", (nome, peso, altura, plano_id))

conexao.commit()
conexao.close()

print("Usuário e planos castrada com sucesso!")