# UM PROFESSOR QUER SORTEAR UM DOS QUATROS ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME ESCOLHIDO 
import random
CandidatoN1 = input("Digite o nome do candidato: ")
CandidatoN2 = input("Digite o nome do candidato: ")
CandidatoN3 = input("Digite o nome do candidato: ")
CandidatoN4 = input("Digite o nome do candidato: ")
 
lista = [CandidatoN4, CandidatoN1, CandidatoN2, CandidatoN3]

escolhido = random.choice(lista)

print("O candidato escolhido é {}".format(escolhido))