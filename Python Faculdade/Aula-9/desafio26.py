frase = str(input('Digite uma frase: ')).strip()
print(f'A letra A aparece {frase.upper().count('A')} vezes na frase.')
print(f'A primeira posição da letra A na frase é: {frase.upper().find('A')+1}')
print(f'A última posição da letra A na frase é: {frase.upper().rfind('A')+1}')