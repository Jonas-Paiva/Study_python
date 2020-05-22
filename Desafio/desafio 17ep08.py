from math import sqrt
cp = float(input('Qual valor do cateto oposto?'))
cd = float(input('Qual valor do cateto adjacente?'))
h2 = (cp**2+cd**2)
hq = sqrt(h2)
print('se o CP é {} e o CD é {}, logo a H é {:.2f} , '.format(cp,cd,hq))