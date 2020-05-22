num = int(input('Escolha qualquer numero inteiro:'))
base = int(input('Qual será a base numerica:\n'
                 '[1]BINÁRIO \n'
                 '[2]OCTAL\n'
                 '[3]HEXADECIMAL\n'
                 'Escolha uma opção:'))
if base == 1:
    print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('TU SEGO SEU DOENTE MENTAL !!!!!\n'
          'Opção invalida. Tente novamente.')
