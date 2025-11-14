# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUE SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATROS ALUNOS E  MOSTRE A ORDEM DOS SORTEADOS
from random import shuffle
aluno1 = str(input("Escreva o nome do Aluno: "))
aluno2 = str(input("Escreva o nome do Aluno: "))
aluno3 = str(input("Escreva o nome do Aluno: "))
aluno4 = str(input("Escreva o nome do Aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print("A sequencia de quem vai apresentar é: {}".format(lista))