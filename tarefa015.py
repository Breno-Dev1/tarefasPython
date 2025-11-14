# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0.15 POR KM RODADO.

kmPercorridos = float(input("Quantos km voce percorreu com o carro? "))
diasAlugados = int(input("Quantos dias foram alugados? "))

valorTotalAPagar = (kmPercorridos * 0.15) + (diasAlugados * 60.00) 

print("Voce percorreu o total de {}km e usou por {} dias, o Valor Total a pagar é R${}".format(kmPercorridos, diasAlugados, valorTotalAPagar))