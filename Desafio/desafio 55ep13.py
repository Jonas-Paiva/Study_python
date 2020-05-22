# Comparação de pesos

# Variáveis: Acumulativas
maior = 0
menor = 0

# Repetição
for c in range(1, 6):
    peso = float(input('Qual é o peso da {} pessoa: '.format(c)))

    # Condição: Camparando os pesos
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior += peso
        if peso < menor:
            menor += peso

# Monstrando na tela
print('O maior peso é {}kg.'.format(maior))
print('O menor peso é {}kg.'.format(menor))