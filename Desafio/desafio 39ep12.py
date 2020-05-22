import datetime
hoje = datetime.date.today().year
print('\033[1:36mForças Armadas Brasileiras\033[m')
print('Faça agora a sua consuta AGORA!')
dia = int(input('Dia de nascimento:'))
mes = int(input('Mês do nascimento:'))
ano = int(input('Ano do nascimento:'))
tempo = (hoje - ano)
if tempo < 18:
    print('Você tem {} anos\n'
          'Ainda falta {} anos para você se alistar.\n'
          'Seu alistamento será em {}'.format(tempo, 18 - tempo, (18-tempo)+hoje))
elif tempo == 18:
    print('Esta na hora de você se alistar.')
elif tempo > 18:
    print('Você tem {} anos e passou {} anos do tempo de se alistar\n'
          'Seu alistamento foi em {}.'.format(tempo, tempo-18, hoje - (tempo-18)))
