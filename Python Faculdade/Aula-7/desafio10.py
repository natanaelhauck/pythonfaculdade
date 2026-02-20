#Us1,00 = R$3,27
r = float(input('Digite quantos reais você tem em sua carteira R$'))
d = r/3.27
print('Com R${:.2f} você pode comprar US${:.2F}'.format(r,d))
# print(f'{d}') >jeito melhor, sem usar .format