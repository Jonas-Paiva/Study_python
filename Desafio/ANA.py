print('Olá !!! meu nome é Ana')
c1 = str(input('Qual é o seu nome?')).strip().upper().split()
print('Oi {}, sou nova aqui na escola'
      '\nEstou tentando fazer novos amigos'.format(c1[0]))
idade = int(input('Quantos anos você tem?'))
if idade >= 18:
    print('Poxa, nem parece que '
          'você é maior de idade,'
          'tem cara de novo!')
    print('eu tenho 18 anos')
else:
    print('Você é muito novinho!!!\n'
          'vou nem fala minha idade\n'
          'se não você vai me chamar de velha kkk')