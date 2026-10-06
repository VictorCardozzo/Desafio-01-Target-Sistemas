dados= {
	"estoque":
	[
	  {
		"codigoProduto": 101,
		"descricaoProduto": "Caneta Azul",
		"estoque": 150
	  },
	  {
		"codigoProduto": 102,
		"descricaoProduto": "Caderno Universitário",
		"estoque": 75
	  },
	  {
		"codigoProduto": 103,
		"descricaoProduto": "Borracha Branca",
		"estoque": 200
	  },
	  {
		"codigoProduto": 104,
		"descricaoProduto": "Lápis Preto HB",
		"estoque": 320
	  },
	  {
		"codigoProduto": 105,
		"descricaoProduto": "Marcador de Texto Amarelo",
		"estoque": 90
	  }
	]
}

historico={}
id_movimentacao=0

while True:

    print('''
[1] Consultar movimentações
[2] Saída de estoque
[3] Sair''')

    resp=int(input('Digite sua opção : '))


    if resp==1:
        if historico=={}:
            print('Não foi feita nenhuma operação no estoque ainda, faça alguma para que seja contabilizado')
        else:
            print(historico)



    if resp ==2:
        codigo=int(input('Informe o codigo do produto: '))
        produto_encontrado=None

        for item in dados["estoque"]:
            if item["codigoProduto"]==codigo:
                produto_encontrado=item

        if produto_encontrado is None:
            print('Produto não encontrado, verifique o codigo e tente novamente')

        else:
            qtd=produto_encontrado["estoque"]
            nome=produto_encontrado["descricaoProduto"]
            retirar=int(input('Deseja retirar quantas unidades? '))

            if retirar >qtd:
                print (f'Operação cancelada! Quantidade indisponível em estoque (Saldo atual: {qtd}).')
            elif retirar<=0:
                print('A quantidade a ser retirada deve ser maior que zero.')
            else:
                id_movimentacao+=1
                produto_encontrado["estoque"]-=retirar

                historico[id_movimentacao]={
                "produto":nome,
                "quantidade":retirar,
                "estoque_final": produto_encontrado["estoque"]
            }
                print(f'Sucesso! O produto {nome}  que estava com {qtd} unidades, agora está com {produto_encontrado["estoque"]} unidades em estoque.')

    if resp==3:
        print('Programa finalizado com sucesso')
        break


