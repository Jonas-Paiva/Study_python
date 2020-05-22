# Palindromos
frase = str(input('Escreva uma frase: ')).upper().strip().split()
junto = ''.join(frase)
inverso = junto[::-1]
if inverso == junto:
    print('{} é = {}'.format(inverso, junto))
else:
    print('{} não é {}'.format(inverso, junto))
