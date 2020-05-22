l = float(input('Qual é a largura da parede?'))
c = float(input('Qual é o comprimento da parede?'))
m = (l*c)
print('Considerando que para cada 2m² é preciso 1L de tinta,\nvocê irá precisar de {:.2f}L de tinta para {:.2f}m² de parede'.format(m/2,m))