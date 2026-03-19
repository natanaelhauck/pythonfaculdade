for c in range(0, 6):
    print('oi')
print('fim')
for d in range(0, 7, 2):
    print(d)
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

i = int(input('início: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')
