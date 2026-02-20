nome = str(input('Qual é o seu nome? '))
if nome == 'Natanael':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é popular')
elif nome in 'Ana':
    print('Que nome bonito')
else: 
    print('Seu nome é comum')
print(f'Tenha uma bom dia {nome}')