p = float(input('Qual o preço do produto? '))
print('O preço do produto é R${:.2f} \nNa nossa liquidação seu produto terá 5% de desconto e o seu novo preço será R${:.2f}'.format(p, p-p*0.05))