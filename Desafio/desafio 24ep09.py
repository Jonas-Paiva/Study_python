cidade = (str(input('Qual é o nome da cidade onde mora?'))).strip()
CM = (cidade.upper())
VouF = ('SANTO'in CM[:5])
print('Então é {} que sua cidade tem Santo no primeiro nome'.format(VouF))