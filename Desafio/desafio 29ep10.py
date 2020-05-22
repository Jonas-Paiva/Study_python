velocidade = int(input(' Qual é a velocidade do carro ?'))
if velocidade > 80:
    print('Você ultrapassou a limite de 80km/h e'
          '\nFoi MULTADO em R$ {},00.'.format((velocidade-80)*7))
else:
    print('Tudo bem, você esta dentro do limite!\n'
          'dirigia sempre com conciência!')
