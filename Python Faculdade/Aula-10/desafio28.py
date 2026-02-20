from random import randint
pc = randint(0, 5)
print(f"""Vamos jogar um desafio! 
Pensei um número inteiro de 1 a 5""")
n = int(input('Qual número você acha que eu pensei? '))
if  n == pc:
    print(f'Parabéns Você venceu (:')
else: 
    print(f'Errou, eu pensei no número {pc}, você perdeu')