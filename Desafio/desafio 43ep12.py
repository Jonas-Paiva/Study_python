# Indice de Massa Corporal
from time import sleep

print('\033[31mIndice de Massa Corporal\033[m: IMC')

# Variaveis
peso = float(input('Seu \033[34mpeso\033[m em Kg: '))
altura = float(input('Sua \033[34maltura\033[m em Metros: '))

# Variaveis De comparação
IMC = (peso/(altura**2))
ideal = 21.7*(altura**2)

print('\033[1:36mANALIZANDO...\033[m')
sleep(2)

# Condição: Categorias do IMC
if IMC < 18.5:
    print('Seu IMC {:.1f}'.format(IMC))
    print('Seu peso é {:.1f}kg.'.format(peso))
    print('Classificação:\033[31m Abaixo do Peso.\033[m')
    print('Você precisa ganhar aproximadamente {:.1f}kg'.format(ideal-peso))
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
