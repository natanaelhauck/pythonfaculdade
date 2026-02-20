número = int(input('Digite um número de 0 a 9999: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número //1000 % 10
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')



