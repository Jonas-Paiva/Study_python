menu = 0

while menu != 6:
    primeiro = int(input('Valor 1: '))
    segundo = int(input('Valor 2 : '))
    menu = 0

    while menu not in (5, 6):

        print('[1]soma\n[2]multiplicação\n[3]maior\n[4]menor\n[5]novo numero\n[6]sair\n')
        menu = int(input('Escolha uma opção: '))

        if menu == 1:
            print('A soma entre {} e {} é = {}'.format(primeiro, segundo, primeiro+segundo))

        if menu == 2:
            print('A multiplicação entre {} e {} é = {}.'.format(primeiro, segundo, primeiro*segundo))

        if menu == 3:
            if primeiro > segundo:
                print('O Maior entre {} e {} é {}'.format(primeiro, segundo, primeiro))
            elif segundo > primeiro:
                print('O Maior entren {} e {} é {}'.format(primeiro, segundo, segundo))
            elif primeiro == segundo:
                print('Os dois são iguais.')

        if menu == 4:
            if primeiro < segundo:
                print(' O Menor entre {} e {} é {}'.format(primeiro, segundo, primeiro))
            elif segundo < primeiro:
                print('O Menor entre {} e {} é {}.'.format(primeiro, segundo, segundo))
            elif primeiro == segundo:
                print('Os dois são iguais.')
        if menu > 6 or menu < 1:
            print('OPÇÂO INVÁLIDA:')

print('Obrigado!!!')
print('Tenha um bom dia!!!')
