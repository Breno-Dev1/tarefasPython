# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVEIS SOBRE ELE 

a = input("Digite algo: ")


print("O tipo primitivo desse valor é: ", type(a))
print("So tem espaço: ",a.isspace())
print("É numerico: ", a.isnumeric())
print("Está em minuscula: ", a.islower())
print("Está em maiuscula? : ", a.isupper())
print("É alfanumerico: ", a.isalnum())
print("É alfabetico: ", a.isalpha())
print("Está Capitalizado:", a.istitle())
