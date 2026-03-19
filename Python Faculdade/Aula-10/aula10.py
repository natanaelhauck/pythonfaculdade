nome = str(input('Qual o seu nome? '))
if nome == 'Natanael':
    print(f'Que nome bonito')
else:
    print(f'Seu nome é comum')
print(f'Bom dia {nome:}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a primeira nota: '))
m = (n1 +n2)/2
print(f'A sua média foi: {m:.2f}')
if m >= 6:
    print(f'Sua nota foi boa')
else: 
    print(f'Sua nota não foi boa')
