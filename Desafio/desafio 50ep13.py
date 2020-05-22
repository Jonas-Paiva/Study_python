# Mostre a soma apenas dos pares.
soma = 0
for c in range(6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
       soma += num
print('A soma dos números pares é {}.'.format(soma))
# Desafio 51 = Desenvolva uma programa que leia seis números inteiros e
