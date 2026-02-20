
nome = str(input('Digite o seu nome completo: ')).strip()
primeironome = nome.split()
print(f'Nome em maiúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
print(f'Total de letras: {len(nome) - nome.count(' ')}')
print(f'Total de letras do primeiro nome: {len(primeironome [0])}')        
