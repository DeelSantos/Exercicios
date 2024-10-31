#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

nome1 = input("Digite o nome do aluno: ")
nome2 = input("Digite o nome do aluno: ")
nome3 = input("Digite o nome do aluno: ")
nome4 = input("Digite o nome do aluno: ")

#Sempre que usar choice par escolher algo deve usar colchetes
sorteio = random.choice([nome1,nome2,nome3,nome4])


print(sorteio)