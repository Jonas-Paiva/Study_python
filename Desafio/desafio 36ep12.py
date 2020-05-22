from time import sleep

nome = str(input('Digite seu nome completo:')).upper().strip().split()
print('Seja Bem-vindo! \033[1;36m{}\033[m'.format(nome[0]))
sleep(2)
print('Empréstimo no \033[1;34mBANCO SONAJ\033[m')
sleep(2)
emprestimo = str(input('Para qual patrimonio você quer o empréstimo ?\n'
                       '\033[1;31mcasa, carro\033[m ou para abrir uma \033[1;31mmicro empresa:\033[m')).upper().strip()
if emprestimo == 'CASA' or 'CARRO' or 'EMPRESA' or 'MICRO EMPRESA':
    patrimonio = float(input('Qual é o \033[32mvalor\033[m da \033[31m{}?\033[m R$'.format(emprestimo)))
    salario = float(input('Qual é o seu salário? R$'))
    tempo = float(input('Em quantos \033[1;34manos\033[m prentende pagar?'))
    print('-_-' * 20)
    print('\033[1;34mANALIZANDO...\033[m')
    print('-_-' * 20)
    sleep(3)
    parcelas = float(patrimonio // (tempo * 12))
    porcentagemS = float(salario * 0.30)
    if parcelas <= porcentagemS:
        print('PARABÉNS {} !!!\n'
              'Seu crédito foi aprovado \n'
              'O valor mensal das parcelas será de R${:.2f}\n'
              'Que esta a baixo dos 30% do seu salário que é R${:.2f}\n'
              'E será pago em {} anos ou {} meses.'.format(nome[0], parcelas, porcentagemS, tempo, tempo * 12))
    else:
        print('Infelizmente seu crédito foi \033[1;31mREPROVADO!!!\033[m.\n'
              'As parcelas de R${:.2f} por mês passam dos 30% do seu salário\n'
              'Que é de R${:.2f} .'.format(parcelas, porcentagemS))
