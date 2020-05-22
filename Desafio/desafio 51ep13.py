#Progressão Aritimetica

 #titulo
print('\033[1:34m-='*20)
print('            10 TERNOS DA PA')
print('-='*20)
print('\033[m')

 #Variáveis
termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÂO da progressão: '))
decimo = termo + (11-1) * razao

 #Codico de repetição
for c in range(termo, decimo, razao):
    print(c, end=' ')
