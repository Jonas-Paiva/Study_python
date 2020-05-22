salario = float(input('Ola\nQual é o seu salário na empressa ?'))
if salario >= 1200:
    print('Você receberar um aumento de 10%\n'
          'De R${:.2f} para R${:.2f}'.format(salario, salario//10 + salario))
else:
    print('Você receberar um aumento de 15%\n'
          'De R${:.2f} para R${:.2f}'.format(salario, salario*0.15 + salario))