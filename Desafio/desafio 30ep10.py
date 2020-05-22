num = int(input('Escreva qualquer número:'))
par = [0, 2, 4, 6, 8]
u = (num//1 % 10)
if u in par:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é impar.'.format(num))
