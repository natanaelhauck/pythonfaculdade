from random import randint 
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Vamos Jogar Jokenpô')
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Escolha sua opção: '))
print('-=' * 11)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 11)
if jogador == 0 and computador == 2 or \
   jogador == 1 and computador == 0 or \
   jogador == 2 and computador == 1:
   print('O jogador venceu')
elif jogador == computador:
   print('Empate')
else:
   print('O computador venceu')