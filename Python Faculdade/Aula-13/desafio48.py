print('Soma dos números ímpares divisíveis por 3, de 1 a 500:')
s = 0
for c in range (1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print (s)
