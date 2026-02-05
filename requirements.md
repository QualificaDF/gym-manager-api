# GymManager API (Academia)

**Foco:** Cálculos matemáticos no Backend e lógica de negócios.

## 1. Gestão Administrativa

* **RF01 - Planos:** Cadastrar tipos de planos (nome, `valor_mensal`). Ex: *"Plano Gold - R$ 100"*, *"Plano Silver - R$ 80"*.
* **RF02 - Alunos:** Cadastrar alunos com nome, altura (em metros), peso (em KG) e vincular a um `id_plano`.

## 2. Saúde e Financeiro (O Core)

* **RF03 - Consulta de IMC:** Rota específica `GET /alunos/{id}/imc`.
    > **Regra de Ouro:** O valor do IMC não deve ficar salvo no banco de dados fixo, pois o peso muda. A API deve calcular na hora da requisição: `peso / (altura * altura)`.
    > A resposta deve incluir a categoria textual (Ex: *"Sobrepeso"*, *"Obesidade"*, *"Peso Ideal"*) baseada em tabela oficial.
* **RF04 - Atualizar Medidas:** Rota simples para atualizar apenas o peso do aluno. Ao consultar o IMC novamente, o valor deve mudar.
* **RF05 - Receita Projetada:** Rota que soma o valor dos planos de todos os alunos ativos para exibir o faturamento mensal total da academia.
