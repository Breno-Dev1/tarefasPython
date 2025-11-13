# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETRO E MILIMETROS 

medida = float(input("Escreva a quantidade de metros: "))
cm = medida * 100 # CENTÍMETROS 
mm = medida * 1000 # MILIMETROS
km = medida * 0.001 # QUILÔMETROS
hm = medida * 0.01 # HECTÓMETRO
dam = medida * 0.1 # DECÂMETRO
dm = medida * 10 # DECIMETROS

print("A medida em km é: {}, hm é: {}, dam é: {}, dm é {}, cm é: {:.0f}. mm é {:.0f}".format(km, hm, dam, dm, cm, mm))
