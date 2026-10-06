🚀 Desafios Técnicos de Programação — Python

Este repositório reúne as soluções desenvolvidas para um processo seletivo, compostas por três desafios práticos de processamento de dados, lógica de negócios e manipulação de estruturas na linguagem Python.
-----------------------------------------------------------------------------
💡 Sobre a Abordagem Técnica

Todas as soluções foram implementadas utilizando recursos nativos do Python, sem dependências externas pesadas. O foco principal da resolução foi demonstrar domínio da lógica de programação e manipulação eficiente das estruturas de dados fundamentais da linguagem.

Principais Conceitos Aplicados:

Dicionários (dict): Utilizados para busca rápida com complexidade $O(1)$, agrupamento de dados por chave (ex: totalização por vendedor) e modelagem de registros estruturados.

Listas (list) e Iterações (for / while): Empregadas para percorrer coleções de dados, realizar filtragens, aplicar regras condicionais por item e manter loops de interação com o usuári

Tratamento e Validação de Dados: Implementação de verificações de consistência (ex: controle de saldo de estoque para evitar quantidades negativas, tratamento de IDs únicos e entradas do usuário).

Estruturação da Regra de Negócio: Separação clara entre a entrada dos dados, o processamento lógico e a exibição de resultados formatados no console.
-------------------------------------------------------------------------------
⚙️ Resumo dos Desafios
1. 📊 Cálculo de Comissões por Venda
Objetivo: Processar uma coleção de vendas e calcular a comissão acumulada por vendedor.

Destaque Lógico: A comissão é calculada venda a venda conforme faixas de valor (0%, 1% ou 5%), e os resultados são agrupados dinamicamente em dicionários.

2. 📦 Gestão e Movimentação de Estoque
Objetivo: Sistema interativo para registrar entradas e saídas de mercadorias no depósito.

Destaque Lógico: Validação de saldo disponível antes de autorizar retiradas, geração de identificador único por operação e manutenção de histórico acumulado em memória.
