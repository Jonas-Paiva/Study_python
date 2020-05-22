nome = str(input('Qual é o seu nome completo ?')).strip().split()
print('Seu primeiro nome é {} e o ultimo é {} '.format(nome[0], nome[len(nome)-1]))
