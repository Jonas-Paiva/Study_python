from time import sleep
a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
c = int(input('Digite outro número:'))
print('-=-'*20)
print('ANALIZANDO...')
print('-=-'*20)
sleep(2)
#ANALIZANDO OS MENORES
menor = a
if a > b and c > b:
    menor = b
if a > c and b > c:
    menor = c
#ANALIZANDO OS MAIORES:
maior = a
if a < b and c < b:
    maior = b
if a < c and b < c:
    maior = c
print('Entre os 3, o menor é {} e o maior é {}.'.format(menor, maior))