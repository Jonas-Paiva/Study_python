print('[7;30;47mVamos descubrir se as 3 retas formaram um triângulo!!!')
print('_-_'*20)
r1 = float(input('Valor da \033[1;31mPRIMEIRA\033[m reta?'))
r2 = float(input('Valor da \033[1;31mSEGUNDA\033[m reta?'))
r3 = float(input('Valor da \033[1;31mTERCEIRA\033[m reta?'))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Com as retas {}cm, {}cm e {}cm você pode montar\n'
          'Um \033[1;32mTRIÂNGULO\033[m.'.format(r1, r2, r3))
else:
    print('Não dá para montar um \033[1;31mTRIÂNGULO\033[m.')
