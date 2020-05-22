impar = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        impar = impar + c
print('Foram {} somados \n'
      'Soma dos impares é {}'.format(cont, impar))
