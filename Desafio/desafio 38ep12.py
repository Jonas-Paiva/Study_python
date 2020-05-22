n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
if n1 > n2:
    print('O \033[1:34mPRIMEIRO\033[m valor é maior.')
elif n1 < n2:
    print('O \033[1:31mSEGUNDO\033[m valor é maior.')
else:
    print('Não exite valor maior, os dois são \033[1;32mIGUAIS.\033[m')
