📅 Cálculo de Juros por Atraso (03-calculo-juros)

Objetivo: Calcular o valor dos juros acumulados com base na data de vencimento e na data atual.

Regra de Negócio:

Aplicação de multa/juros de 2,5% ao dia sobre o valor original em caso de atraso.

Isenção de cobrança caso o título esteja em dia.

Destaque de Lógica: Conversão de texto para objeto datetime com strptime(), cálculo do intervalo em dias (.days) e aplicação proporcional da taxa.




