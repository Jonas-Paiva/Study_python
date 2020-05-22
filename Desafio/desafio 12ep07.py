p = float(input('Qual o preço do produto?'))
d = (p/100)
print('Pagando no dinheiro terá 5% de desconto, ficará R${:.2f}'.format(p-d*5))