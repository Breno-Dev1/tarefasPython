# FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5$ DE DESCONTO

preco = float(input("Digite o preço do Produto: "))
desconto = preco - (preco * 5/100)

print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${}".format(preco, desconto))