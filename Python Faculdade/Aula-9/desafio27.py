nome = str(input('Digite o seu nome completo: ')).strip()
name = nome.split()
print(f'Seu primeiro nome é: {name[0]}')
print(f'Seu último nome é: {name[len(name)-1]}')
