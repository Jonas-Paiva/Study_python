from datetime import datetime
print('\033[1:34mConfederação Nacional De Natação\033[m')
print('Digite o ano de nascimento para entrar na competição na categoria adequada.')
ano = int(input('Ano de nascimento: '))
hoje = datetime.today().year
idade = hoje - ano
if idade <= 9:
    print('Você tem {} anos, sua categoria é MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos, sua categoria é INFÂNTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos, sua categoria é JUNIOR.'.format(idade))
elif idade > 19 and idade <=25:
    print('Você tem {} anos, sua categoria é SÊNIOR.'.format(idade))
elif idade > 25:
    print('Você tem {} anos, sua categoria é MASTER.'.format(idade))
