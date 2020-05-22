# Número Primo

# Variavel
num = int(input('Digite um número:'))
print('DIVISÍVEL POR:')

# Variavel: Contador
div = 0

# Condição: Divisivel por
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        div += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' \033[m')

# Condição: Número PRIMO
if div == 2:
    print('\n {} é número PRIMO.\n'
          'Ele foi divisivel  {} vezes '.format(num, div))
else:
    print('\n{} NÂO é PRIMO.\n'
          'Ele foi divisivel  {} vezes '.format(num, div))
