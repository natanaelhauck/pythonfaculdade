i = int(input('Olá Atleta! Digite a sua idade: '))
if i < 10:
    print('Você é da categoria mirim! ')
elif i > 9 and i < 15: 
    print('Você é da categoria infantil! ')
elif i > 14 and i < 20: 
    print('Você é da categoria júnior! ')
elif i > 19 and i < 21: 
    print('Você é da categoria sênior! ')
else: 
    print('Você é da categoria master')
