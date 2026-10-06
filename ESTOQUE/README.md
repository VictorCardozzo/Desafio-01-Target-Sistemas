2. 📦 Gestão e Movimentação de Estoque (02-gestao-estoque)
O que faz: Mantém um menu interativo no terminal para consultar movimentações e registrar entradas/saídas de mercadorias no depósito.

Como foi feito:

Foi estruturado o programa dentro de um laço contínuo while True com opções numéricas (1 para consultar movimentações, 2 para saída de estoque , 3 para sair do programa).

Ao informar o código do produto, fazemos uma busca com o laço for na lista de estoque. Se o produto for localizado (produto_encontrado is not None), prosseguimos; caso contrário, informamos que o código não existe.

Na operação de saída, aplicamos uma trava de segurança (if retirar > qtd) para impedir a atualização caso o saldo em estoque seja insuficiente.

Se o saldo for válido, incrementamos um contador numérico (id_movimentacao += 1), subtraímos a quantidade do estoque em memória (produto_encontrado["estoque"] -= retirar) e salvamos o registro no dicionário historico.
