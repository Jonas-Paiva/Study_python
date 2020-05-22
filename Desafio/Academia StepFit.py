# JUNTANDO TUDO : Desafios 43, 44.
from datetime import date

print('\033[1:34mACADEMIA StepFIT\033[m')
n1 = int(input('Quantos Cadastros: '))

# FORMULÁRIO
for c in range(1, n1+1):

    # VARIÁVEIS
    print('\nCADASTRO {}'.format(c))
    nome = str(input('Qual é o seu nome ? : '))
    nascimento = int(input('Ano de nascimento: '))
    peso = float(input('Qual é o seu peso em kg: '))
    altura = float(input('Qual é a sua altura em METRO: '))
    print('Qual é forma de pagamento:\n'
          '[1] Dinheiro = 10% de desconto\n'
          '[2] Cartão = em até 2x sem juros')
    forma = int(input('Escolha um Opção: '))

    # VARIÁVEIS: Comparativas
    idade = nascimento - date.today().year
    IMC = peso / (altura ** 2)
    ideal = 21.7 * (altura ** 2)
    mes = date.today().month

    # CONDIÇÃO: FORMA DE PAGAMENTO

    #DINHEIRO
    if forma == 1:
        print('\n')
        print('\33[1:34mINFOMAÇÂO DO CLIENTE\033[m')
        print('O valor da mensalidade é R${:.2f} por mês.'.format(120-(120*0.10)))

    #CARTÃO
    else:
        print('\n')
        print('\33[1:34mINFOMAÇÂO DO CLIENTE\033[m')
        pacelas = int(input('Em Quantas vezes: '))
        if pacelas <= 2:
            print('A mensalidade do mês {} foi divida em {}x de R${:.2f} sem juros.'.format(mes, pacelas, 120/pacelas))
        elif pacelas > 2:
            print('A mesalidade do mês {} foi divida em {}x de R${:.2f}\n'
                  'Com 5% de JUROS'.format(mes,pacelas,(120+(120*0.05))/pacelas ))

    # Condição: Categorias do IMC
    if IMC < 18.5:
        print('Seu IMC {:.1f}'.format(IMC))
        print('Seu peso é {:.1f}kg.'.format(peso))
        print('Classificação:\033[31m Abaixo do Peso.\033[m')
        print('Você precisa ganhar aproximadamente {:.1f}kg'.format(ideal - peso))
        print('Seu peso ideal é aproximadamente {:.1f}kg'.format(ideal))

    elif IMC >= 18.5 and IMC < 25:
        print('Seu IMC é {:.1f}.'.format(IMC))
        print('Seu peso é {:.1f}kg.'.format(peso))
        print('Classificação:\033[31m Peso ideal\033[m')
        print('Seu peso ideal é aproximadamente {:.1f}kg'.format(ideal))

    elif IMC >= 25 and IMC < 30:
        print('Seu IMC é {:.1f}.'.format(IMC))
        print('Seu peso é {:.1f}kg.'.format(peso))
        print('Classificação: \033[31mSobrepeso\033[m')
        print('Você precisa perder aproximadamente {:.1f}kg'.format(peso - ideal))
        print('Seu peso ideal é aproximadamente {:.1f}kg'.format(ideal))

    elif IMC >= 30 and IMC < 40:
        print('Seu IMC é {:.1f}.'.format(IMC))
        print('Seu peso é {:.1f}kg.'.format(peso))
        print('Classificação: \033[31mObsidade\033[m')
        print('Você precisa perder aproximadamente {:.1f}kg'.format(peso - ideal))
        print('Seu peso ideal é aproximadamente {:.1f}kg'.format(ideal))

    elif IMC >= 40:
        print('Seu IMC é {:.1f}.'.format(IMC))
        print('Seu peso é {:.1f}kg.'.format(peso))
        print('Classifição: \033[31mObsidade Mórbida\033[m')
        print('Você precisa perder aproximadamente {:.1f}kg'.format(peso - ideal))
        print('Seu peso ideal é aproximadamente {:.1f}kg'.format(ideal))