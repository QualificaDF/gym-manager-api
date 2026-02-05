from flask import Blueprint, request, jsonify
from db import get_connection
from utils import calcular_imc, categoria_imc
from auth.auth_decorator import *

api = Blueprint("api", __name__)


@api.route("/alunos", methods=["GET"])
@internal_auth_required
def listar_alunos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, peso, altura, plano_id FROM alunos
    """)
    alunos = cursor.fetchall()
    conn.close()

    alunos_list = []
    for aluno in alunos:
        imc = calcular_imc(aluno[2], aluno[3])
        alunos_list.append({
            "id": aluno[0],
            "nome": aluno[1],
            "peso": aluno[2],
            "altura": aluno[3],
            "plano_id": aluno[4],
            "imc": imc,
            "categoria_imc": categoria_imc(imc)
        })

    return jsonify(alunos_list), 200


@api.route("/alunos", methods=["POST"])
@internal_auth_required
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
@internal_auth_required
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
@internal_auth_required
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
@internal_auth_required
def faturamento():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(p.valor_mensal)
        FROM alunos a
        JOIN planos p ON a.plano_id = p.id
    """)
    resultado = cursor.fetchone()[0]
    total = round(resultado, 2) if resultado else 0.0
    conn.close()

    return jsonify({
        "faturamento_total": total 
    })


@api.route("/alunos/<int:id>", methods=["DELETE"])
@internal_auth_required
def deletar_aluno(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"erro": "Aluno não encontrado"}), 404

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Aluno deletado com sucesso"})