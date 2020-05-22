from random import shuffle
n1 = (input('Nome do grupo 1 ?'))
n2 = (input('Nome do grupo 2 ?'))
n3 = (input('Nome do grupo 3 ?'))
n4 = (input('Nome do grupo 4 ?'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem dos grupos é')
print(lista)
