# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM °C E converta para °F

temperatura = int(input("Qual a temperatura que esta fazendo na sua cidade? "))
F = temperatura * 9/5 + 32

print("A temperatura {}°C em Fahrenheit é {}°F".format(temperatura, F))
