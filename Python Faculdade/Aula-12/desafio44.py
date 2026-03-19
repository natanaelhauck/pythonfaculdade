vp = float(input('Qual o valor do produto: R$'))
print(''' FORMAS DE PAGAMENTO 
 [1] À vista dinheiro/cheque
 [2] À vista cartão)
 [3] parcelado no cartão ''')
cp = int(input('Escolha a forma de pagamento: '))

if cp == 1:
    print(f'Você recebeu um desconto de 10%, o valor a ser pago será R${vp - vp * 0.1:.2f}')
elif cp == 2:
    print(f'Você recebeu um desconto de 5%, o valor a ser pago será R${vp - vp * 0.05:.2f}')
elif cp == 3:
    p = int(input('Em quantas vezes você vai parcelar? '))
    if p == 2:
        print(f'Você não recebeu desconto, o valor a ser pago será R${vp:.2f}')
    elif p >= 3:
        print(f'Com o parcelamento, o juros será de 20%. O valor a ser total a ser pago será R${vp}, em {p} parcelas de R${(vp + vp * 0.2) / p:.2f}')
    else:
        print('Opção inválida')
else:
    print('Opção inválida')