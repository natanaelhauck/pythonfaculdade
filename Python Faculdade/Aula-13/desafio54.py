from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(7):
    an = int(input('Digite o ano de nascimento: '))
    i = ano - an
    if i >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} pessoas são menores de idade')
