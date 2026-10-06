from datetime import datetime
print("--- CÁLCULO DE JUROS POR ATRASO ---")

valororiginal=float(input('Digite o valor inicial da conta: R$ '))
datavencimentost=input('Digite a data de vencimento (formato DD/MM/AAAA) ')

datavencimento=datetime.strptime(datavencimentost,"%d/%m/%Y" ).date()
datahoje=datetime.now().date()
diasatraso=(datahoje-datavencimento).days

taxadiaria=0.025

if diasatraso>0:
    
    jurostotal=valororiginal *(taxadiaria*diasatraso)
    total=valororiginal+jurostotal

    print("\n--- RESUMO DO CÁLCULO ---")
    print(f"• Data de Vencimento: {datavencimento.strftime('%d/%m/%Y')}")
    print(f"• Data de Hoje:       {datahoje.strftime('%d/%m/%Y')}")
    print(f"• Dias em Atraso:     {diasatraso} dia(s)")
    print(f"• Valor dos Juros:    R$ {jurostotal:.2f} ({diasatraso}x 2,5%)")
    print(f"• Valor Total a Pagar: R$ {total:.2f}")

else:
    print("\n✅ O título está em dia! Não há cobrança de juros.")
    print(f"• Valor a Pagar: R$ {valororiginal:.2f}")
