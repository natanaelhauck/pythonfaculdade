n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'Sua média foi {m}, você foi reprovado! ')
elif m >= 5 and m < 7:
    print(f'Sua média foi {m}, você está em recuperação! ')
else: 
    print(f'Sua média foi {m}, você foi aprovado! ')