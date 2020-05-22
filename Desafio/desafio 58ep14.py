from random import randint

print('Vamos brincar de adivinhar:')

jogador = int(input('Escolha um Número de 0 à 10: '))
while jogador >= 10 or jogador <= 0:
    jogador = int(input('OPÇÂO INVÁLIDA: Escolha entre 0 à 10: '))
computador = randint(0, 10)
vezes = 1

while jogador != computador:
    print('>'*25)
    if jogador < computador:
        print('Mais um pouco... ')
    if jogador > computador:
        print('Menos um pouco...')
    jogador = int(input('Tente novamente: '))
    vezes = vezes + 1
    print('>' * 25)

print('Você acertou na {}ª vez !!!'.format(vezes))
print('Computador pensou em {}\n''Jogador escolheu em {}.'.format(computador, jogador))
