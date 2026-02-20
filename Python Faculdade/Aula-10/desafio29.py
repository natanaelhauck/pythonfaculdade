v = float(input('Qual a velocidade do carro em Km/h? '))
m = 7 * (v-80)
if v > 80:
    print(f'Você foi multado por exceder o limite de velocidade!')
    print(f'O valor da multa é R$: {m}')
else: 
    print(f'Você estava dentro do limite de velocidade')