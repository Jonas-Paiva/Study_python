# Analize de DADOS

# Variaveis Acumuladivas.
media = 0

# Masculino
hnome = 0
mediaH = 0
Nh = 0
velho = 0
vintao = 0

# Feminino
mediaF = 0
Nf = 0
Fnome = 0
velha = 0
vintona = 0

c = int(input('Quantos cadastos:'))

# Coletando dados
for p in range(1, c+1):

    print('\n\033[1:31m=-=-=-= {} PESSOA.=-=--=-=--\033[m'.format(p))
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M]ou[F]:')).upper().strip()
    media += idade

    # MASCULINO
    if sexo == 'M':

        # Media masculina.
        mediaH += idade
        Nh += 1

        # Mais velho .
        if idade > velho:
            velho = idade
            hnome = nome

        # Menores de 20.
        if idade <= 20:
            vintao += 1

    # FEMININO
    elif sexo == 'F':

        # Media Feminina
        mediaF += idade
        Nf += 1

        # Mais velha.
        if idade > velha:
            velha = idade
            Fnome = nome

        # Menores de 20.
        if idade <= 20:
            vintona += 1

# Caso não tenha nenhum MASCULINO ou FEMENINO.
if vintao == 0:
    vintao = 'Não tem'
if vintona == 0:
    vintona = 'Não tem'
if Nf == 0:
    Nf = 1
if Nh == 0:
    Nh = 1

# Media de idade
print('\n\033[1:34mDADOS COLETADOS\033[m')
print('\nA idade média é {:.1f} anos.'.format(media/c))
print('Media masculina {:.1f} anos.'.format(mediaH/Nh))
print('Media feminina {:.1f} anos.'.format(mediaF/Nf))

# Mais velho
print('\nO homem mais velho é {} e tem {} anos.'.format(hnome, velho))
print('A mulher mais velha é {} e tem {} anos.'.format(Fnome, velha))

# Pessoas com menos de 20 anos
print('\n{} mulher(s) menor de 20 anos'.format(vintona))
print('{} homem(s) menor de 20 anos'.format(vintao))
