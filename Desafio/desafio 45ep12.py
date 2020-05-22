from random import choice
from time import sleep
print('\033[1:34mVamos jogar JOKENPÔ\033[m')
nome = str(input('Qual é o seu nome? ')).strip().upper()
print('Escolha uma opção \033[1:34m{}\033[m\n'
      'PEDRA\n'
      'PAPEL\n'''
      'TESOURA.'.format(nome))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = str(input('Escreva uma opção: ')).upper().strip()
computador = choice(lista)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=-'*20)
if computador == 'PEDRA':
    if jogador == 'PEDRA':
        print('EMPATE!!!')
        print('Computador jogou {}'.format(computador))
    elif jogador == 'PAPEL':
        print('Computador PERDEU!!!')
        print('Computador jogou {}'.format(computador))
    elif jogador == 'TESOURA':
        print('Computador ganhou!!!')
        print('Computador jogou {}'.format(computador))
if computador == 'PAPEL':
    if jogador == 'PAPEL':
        print('EMPATE!!!')
        print('Computador jogou {}'.format(computador))
    elif jogador == 'TESOURA':
        print('Computador PERDEU!!!')
        print('Computador jogou {}'.format(computador))
    elif jogador == 'PEDRA':
        print('Computador ganhou!!!')
        print('Computador jogou {}'.format(computador))
if computador == 'TESOURA':
    if jogador == 'TESOURA':
        print('EMPATE!!!')
        print('Computador jogou {}'.format(computador))
    elif jogador == 'PEDRA':
        print('Computador PERDEU!!!')
        print('Computador jogou {}'.format(computador))
    elif jogador == 'PAPEL':
        print('Computador ganhou!!!')
        print('Computador jogou {}'.format(computador))
print('-=-'*20)
if jogador == 'PEDRA':
    if computador == 'PEDRA':
        print('EMPATE!!!')
        print('{} jogou: {}'.format(nome, jogador))
    elif computador == 'PAPEL':
        print('{} PERDEU!!!'.format(nome))
        print('{} jogou: {}'.format(nome, jogador))
    elif computador == 'TESOURA':
        print('{} ganhou!!!'.format(nome))
        print('{} jogou: {}'.format(nome, jogador))
if jogador == 'PAPEL':
    if computador == 'PAPEL':
        print('EMPATE!!!')
        print('{} jogou: {}'.format(nome, jogador))
    elif computador == 'TESOURA':
        print('{} PERDEU!!!'.format(nome))
        print('{} jogou: {}'.format(nome, jogador))
    elif computador == 'PEDRA':
        print('{} ganhou!!!'.format(nome))
        print('{} jogou: {}'.format(nome, jogador))
if jogador == 'TESOURA':
    if computador == 'TESOURA':
        print('EMPATE!!!')
        print('{} jogou: {}'.format(nome, jogador))
    elif computador == 'PEDRA':
        print('{} PERDEU!!!'.format(nome))
        print('{} jogou: {}'.format(nome, jogador))
    elif computador == 'PAPEL':
        print('{} ganhou!!!'.format(nome))
        print('{} jogou: {}'.format(nome, jogador))
print('-=-'*20)
