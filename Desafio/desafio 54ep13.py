from datetime import date
from time import sleep

# Variáveis: Acumulativas.
maioridade = 0
menor = 0
velho = 0
novo = 0

# Variável de comparação.
demaior = 21
atual = date.today().year

# Registrar o ano de nascimento.
for c in range(1, 8):
    ano = int(input('{}: Ano de Nascimento:'.format(c)))
    nascimento = (atual - ano)

    # Condição: Quantos maiores e menores de idade há.
    if nascimento >= demaior:
        maioridade += 1
    elif nascimento < demaior:
        menor += 1

    # Candição: Qual é o mais velho e o mais novo.
    if c == 1:
        velho = nascimento
        novo = nascimento
    else:
        if nascimento > velho:
         velho = nascimento
        if nascimento < novo:
         novo = nascimento

# Mostrando na dela
print('\033[1:32m-=-'*20)
print('ANALIZANDO...')
print('-=-'*20)
sleep(2)
print('\033[1:34mDADOS DE NATALIDADE\033[m')
print('  Tem {} pessoas maiores de 21 e {} menores '.format(maioridade, menor))
print('  O mais velho tem {} anos '.format(velho))
print('  E o mais novo tem {} anos'.format(novo))
