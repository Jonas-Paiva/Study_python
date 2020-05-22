print('CAIXA')
valor = float(input('Valor do produto: R$'))
print('[1]Dinheiro\n'
      '[2]Cheque.\n'
      '[3]Débito.\n'
      '[4]Crédito.')
formas = int(input('Digite uma Opção: '))
if formas == 1 or formas == 2:
    dinheiro = valor - (valor * 0.10)
    print('Terá o desconto de 10%.')
    print('De R${:.2f} ficará R${:.2f}.'.format(valor, dinheiro))
elif formas == 3:
    cartao1 = valor - (valor * 0.05)
    print('Terá o desconto de 5%.')
    print('De R${:.2f} ficará R${:.2f}.'.format(valor, cartao1))
elif formas == 4:
    parcelas = int(input('Em quantas vezes: '))
    if parcelas == 2:
        print('O valor de R${:.2f}\n'
              'Ficará por R${:.2f} em 2X sem juros.'.format(valor, valor/parcelas))
    elif parcelas > 2:
        cartao3 = (valor + (valor * 0.20)) / parcelas
        print('O valor de R${:.2f}\n'
              'Ficará por R${:.2f} em {}X com 20% de juros.'.format(valor, cartao3, parcelas))
