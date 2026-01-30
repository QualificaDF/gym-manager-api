### GymManager API (Academia)

**Cenário:** Controle de alunos, planos e cálculo de saúde simples.
**Desafio de Lógica:** Cálculo Matemático e Categorização.

#### 🗄️ Entidades (Banco de Dados)
* **Planos:** `id`, `nome` (Mensal, Anual), `valor_mensal`.
* **Alunos:** `id`, `nome`, `peso`, `altura`, `plano_id` (FK).

#### 🔌 Requisitos Funcionais (Endpoints)

* `POST /alunos`
    * Cadastra o aluno vinculando a um plano.

* `GET /alunos/<id>/imc`
    * **Regra de Ouro:** Não salva o IMC no banco. A API deve calcular na hora ($Peso / Altura^2$) e retornar o valor junto com a categoria (Ex: "24.5 - Peso Ideal", "28.0 - Sobrepeso").

* `GET /faturamento`
    * Soma o valor de todos os planos ativos dos alunos cadastrados para prever a receita mensal.

* `PUT /alunos/<id>/trocar_plano`
    * Permite o aluno mudar de plano (Update de FK).

* `GET /alunos/plano/<nome_plano>`
    * Lista todos os alunos que estão no plano "Anual", por exemplo.
