sexo = str(input('Qual é o seu SEXO [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    print('Opção inválida')
    sexo = str(input('\ndigite novamente [M/F]:')).upper().strip()[0]
print('\nObrigado !!!')
print('Sexo {} foi resistrado'.format(sexo))
