# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import hypot
co = float(input("Qual o comprimento do Cateto Oposto: "))
ca = float(input("Qual o comprimento do Cateto Adjacente: "))
ch = hypot(co, ca)
print(" A hipotenusa vai medir {:.2f}".format(ch))