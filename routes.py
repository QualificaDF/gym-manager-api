from flask import Blueprint, request, jsonify
from db import get_connection
from utils import calcular_imc, categoria_imc

api = Blueprint("api", __name__)


@api.route("/alunos", methods=["POST"])
def criar_aluno():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "JSON inválido"}), 400

    nome = dados.get("nome")
    peso = dados.get("peso")
    altura = dados.get("altura")
    plano_id = dados.get("plano_id")

    if not nome or not peso or not altura or not plano_id:
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alunos (nome, peso, altura, plano_id)
        VALUES (?, ?, ?, ?)
    """, (nome, peso, altura, plano_id))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Aluno cadastrado com sucesso"}), 201



@api.route("/alunos/<int:aluno_id>/imc", methods=["GET"])
def imc_aluno(aluno_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT peso, altura FROM alunos WHERE id = ?",
        (aluno_id,)
    )
    aluno = cursor.fetchone()
    conn.close()

    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    peso, altura = aluno
    imc = calcular_imc(peso, altura)

    return jsonify({
        "imc": imc,
        "categoria": categoria_imc(imc)
    })



@api.route("/alunos/<int:aluno_id>/trocar_plano", methods=["PUT"])
def trocar_plano(aluno_id):
    dados = request.get_json()

    if not dados or "plano_id" not in dados:
        return jsonify({"erro": "plano_id é obrigatório"}), 400

    novo_plano = dados["plano_id"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE alunos SET plano_id = ? WHERE id = ?",
        (novo_plano, aluno_id)
    )

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"erro": "Aluno não encontrado"}), 404

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Plano atualizado com sucesso"})



@api.route("/faturamento", methods=["GET"])
def faturamento():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(p.valor_mensal)
        FROM alunos a
        JOIN planos p ON a.plano_id = p.id
    """)

    total = cursor.fetchone()[0]
    conn.close()

    return jsonify({
        "faturamento_total": total if total else 0
    })
