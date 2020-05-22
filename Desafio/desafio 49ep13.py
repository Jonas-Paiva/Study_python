n = int(input('Tabuada de multiplicação de : '))
for c in range(1, 11):
     print('{}x{} = {}'.format(n, c, n*c))
print('\nHEXADECIMAL')
for c in range(1, 11):
    h = hex(n*c)
    print('{}x{}= {}'.format(n, c, h[2:]))