sf = float(input('Qual é o seu salário ?'))
p = (sf/100)
print('Se você receber um aumento de 15% seu salário ficará R${:.2f}\n menos R$200 de passagem, fica R${:.2f}'.format(sf+p*15, (sf+p*15)-200))
