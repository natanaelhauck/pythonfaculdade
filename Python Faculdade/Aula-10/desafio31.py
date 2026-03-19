d = float(input('Qual a distância da viagem em Km? '))
if d <=200: 
    p = d * 0.50
else:
    p = d * 0.45
print(f'O valor da passagem será R$ {p:.2f}')
    
    
