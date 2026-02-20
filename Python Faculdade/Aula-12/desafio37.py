n = int(input('Digite o número inteiro que você quer converter: '))
c = int(input("""Escolha a base de conversão
1: binário
2: octal
3: hexadecimal 
Digite apenas o número correspondente (1 a 3): """))
if c == 1:
    print(f'O número {n} em binário é representado por: {bin(n)[2:]}')
elif c == 2:
    print(f'O número {n} em octal é representado por: {oct(n)[2:]}')
elif c == 3:
    print(f'O número {n} em hexadecimal é representado por: {hex(n)[2:]}')    
else:
    print('Opção inválida" Escolha 1, 2 ou 3.')