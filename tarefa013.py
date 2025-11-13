# FAÇA UM ALGORITIMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO, COM 15% DE AUMENTO 

salarioFuncionario = float(input("Qual o salario do Funcionario? R$"))
novoSalario = salarioFuncionario + (salarioFuncionario * 15/100)

print("O salario do Funcionario é R${}, com o reajuste de 15% o salario ira ficar R${:.3f}". format(salarioFuncionario, novoSalario))