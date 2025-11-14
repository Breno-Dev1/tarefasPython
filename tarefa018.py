# FAÇA UM PROGRAMA QUE LEIA O ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DE SENO, COSSENO E TANGENTE DESSE ANGULO 
from math import radians, cos, sin, tan 
angulo = float(input("Escreva o Angulo: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O angulo de {} tem o Seno de {:.2f}, o Consseno de {:.2f} e a Tangente de {:.2f}".format(angulo, seno, cosseno, tangente))