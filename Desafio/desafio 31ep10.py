print('Olá, bem-vindo !')
distância = float(input('Qual é a distancia da sua viagem em km ?'))
if distância <= 200:
    print('Sua viagem ficará por R${:.2f}.'.format(distância*0.50))
else:
    print('Sua viagem terá um desconto!'
          '\nFicará por R${:.2f}.'.format(distância*0.45))