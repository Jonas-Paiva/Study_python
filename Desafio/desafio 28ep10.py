from random import randint
from time import sleep  #Controla o atraso da leitura dos comando#

print('Vamos brincar de adivinha ?')
jogador = int(input('Estou pensando em um número de  0 a 5, qual é?'))
print('-=-'*20)
print('ANALIZANDO...')
print('-=-'*20)
sleep(2)#Valor em SEGUNDOS#
computador = randint(0, 5)
if jogador == computador:
    print('PARABÉNS você acetou!\n'
          'EU em pensei em {} também.'.format(computador))
else:
    print('Errou kkk, eu pensei em {} e vc em {}.'.format(computador, jogador))