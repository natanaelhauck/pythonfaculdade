print('Olá, vamos calcular a aprovação do seu empréstimo para comprar a sua casa! ')
casa = float(input('Digite o valor da casa: R$ '))
salário = float(input('Digite o seu salário: R$ '))
tempo = int(input('Digite em quantos anos você vai pagar a casa: '))
prestação = casa / (tempo * 12)
if prestação <= salário * 0.3:
    print(f'Empréstimo aceito! A prestação mensal será de R$ {prestação:.2f}')
else: 
    print(f'Empréstimo negado! A prestação de R${prestação:.2f} excedeu os 30% (R${salário * 0.3:.2f}) do seu salário (R${salário:.2f})')
    