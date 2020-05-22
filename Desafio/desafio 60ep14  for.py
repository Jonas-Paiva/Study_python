#fatorial
print('\033[1:32mFATORIAL DE:\033[m')
num = int(input('Digite um número: '))
mult = 1
for c in range(num, 0, -1):
    print(c, end='x',)
    mult *= c
print('\033[1:34m=', mult)