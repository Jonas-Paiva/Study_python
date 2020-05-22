#fatorial

num = int(input('Digite um número: '))
c = 0
multi = 1
while num > c:
    print(num, end='x')
    multi *= num
    num -= 1
print('=', multi)
