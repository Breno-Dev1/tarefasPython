#FAÇA UM PRGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2m²

larg = float(input("Largura da Parede: "))
alt = float(input("Altura da Parede: "))
area = larg * alt
tinta = area / 2 
print("A sua parede tem a dimenão de {} x {} e a sua área é de {}m², você vai precisa de {}L para pintar toda a sua parede".format(larg, alt, area, tinta ))

