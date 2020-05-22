print('Vamos calcular a sua media')
nota1 = float(input('Nota do \033[1:32mTESTE\033[m: '))
nota2 = float(input('Nota da \033[1:32mPROVA\033[m: '))
media = (nota1+nota2)/2
if media < 5:
    print('Sua Media é {:.1f}\n'
          '\033[1:31mREPROVADO!!!\033[m'.format(media))
elif media >= 5 and media < 7:
    print('Sua Media é {:.1f}, está muito baixa\n'
          'Você vai ter que fazer RECUPERAÇÃO.'.format(media))
elif media >= 7:
    print('Sua media é {:.1f}\n'
          'PARABÉNS, Você foi APROVADO.'.format(media))
