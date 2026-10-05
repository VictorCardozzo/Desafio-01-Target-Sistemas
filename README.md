📊 Desafio Técnico: Cálculo de Comissões de Vendas


Este projeto consiste em um script em Python desenvolvido para processar um conjunto de dados de vendas de uma equipe comercial, aplicando regras de comissão dinâmicas sobre cada transação e gerando um relatório consolidado com os ganhos de cada vendedor.

🎯 Objetivo
Ler uma estrutura de dados de vendas em formato JSON/Dicionário e calcular a comissão acumulada de cada funcionário com base no valor de cada venda individual.

Faixa de Valor da Venda,% de Comissão
"Abaixo de R$ 100,00",0% (Não gera comissão)
"De R$ 100,00 até R$ 499,99 (Abaixo de R$ 500,00)",1%
"R$ 500,00 ou mais",5%

🛠️ Tecnologias Utilizadas
Python 3.x

Estruturas de dados nativas: Dicionários (dict) e Listas (list).

⚙️ Como Funciona o Algoritmo
Mapeamento das Vendas: O script percorre cada item da lista de vendas.

Cálculo da Comissão Individual: Verifica o valor da venda com estruturas condicionais (if / elif / else) para aplicar a porcentagem correspondente (0%, 1% ou 5%).

Agrupamento por Vendedor: Utiliza dicionários em memória (vendas_totais e comissoes) para acumular o valor total vendido e a comissão acumulada de cada vendedor.

Exibição do Relatório: Percorre o dicionário gerado e exibe no console o resumo por vendedor com formatação de moeda em duas casas decimais.

🚀 Como Executar o Projetos
Pré-requisitos: Certifique-se de ter o Python 3 instalado em sua máquina.

Clonar/Baixar o código:
https://github.com/VictorCardozzo/Desafio-01-Target-Sistemas.git
cd Desafio-01-Target-Sistemas

📋 Exemplo de Saída no Terminal
Resultado das comissões:
João Silva vendeu R$10754.70, e ficou com o total de 11279.96 com as comissoes
Maria Souza vendeu R$9683.30, e ficou com o total de 10166.78 com as comissoes
Carlos Oliveira vendeu R$7927.80, e ficou com o total de 8327.68 com as comissoes
Ana Lima vendeu R$8763.95, e ficou com o total de 9211.83 com as comissoes

