r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3 or r1 + r3 > r2 or r2 + r3 > r1:
    print('Com essas três retas é possível formar um triângulo')
else: 
    print('Com essas três retas não é possível formar um triângulo')