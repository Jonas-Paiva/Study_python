# PA com while
# an = a1 +(n-1).r
print('Progreção Aritimetica')
termo = int(input('Qual o primeira termo: '))
razao = int(input('Qual a razão de PA: '))
an = int(input('Qual ultimo termo: '))
print('=+'*20)
const = 1
pa = termo

while const <= an:
    print(pa, end='>')
    const += 1
    pa += razao

print('fim...')
