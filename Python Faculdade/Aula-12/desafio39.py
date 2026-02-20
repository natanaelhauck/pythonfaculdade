from datetime import date
nascimento  = int(input('Digite o seu ano de nascimento '))
ano = date.today().year
if ano - nascimento < 18:
    print(f'Você ainda vai se alistar, falta { 18 - (ano - nascimento)} ano(s)')
elif ano - nascimento == 18:
    print(f'Você já deve se alistar!')
else:
    print(f'Você já deveria ter se alistado há {(ano - nascimento) - 18} ano(s)')