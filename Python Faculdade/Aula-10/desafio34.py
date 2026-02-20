s = float(input('Digite o seu salário: R$'))
if s > 1250:
    a = s * 0.1
    print(f'Com o aumento de 10%, o seu salário será R$ {s + a:.2f}')
else: 
    a = s * 0.15
    print(f'Com o aumento de 15%, o seu salário será R$ {s + a:.2f}')