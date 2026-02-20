p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))
imc = p / (a ** 2)

if imc < 18.5:
    print(f'O seu imc é {imc:.2f}, você está abaixo do peso ideal')
elif imc >= 18.5 and imc <= 25:
    print(f'O seu imc é {imc:.2f}, você está dentro do peso ideal')
elif imc > 25 and imc < 30:
    print(f'O seu imc é {imc:.2f}, você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'O seu imc é {imc:.2f}, você está com obesidade')
else: 
    print(f'O seu imc é {imc:.2f}, você está com obesidade mórbida')