frase = str(input('Escreva um poema:')).strip()
f = str(frase.upper())
print('Nesse poema tem {} letras A\nO primeiro A está na {} letra\nO Último esta na letra {}'
      .format(f.count('A'), f.find('A')+1, f.rfind('A')-f.count(' ')+1))