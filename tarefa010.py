# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR

real = float(input("Quanto de Dinheiro voce tem na carteira?  R$ "))
dolar = real / 5.30
euro = real / 6.17

print("Com R${:.2f} voce pode comprar US${:.2f} e €$ {:.2f}".format(real, dolar, euro))