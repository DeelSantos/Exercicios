#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math 

num = float(input("Digite um valor: "))

inteiro = math.trunc(num)

print(f"O valor digitado foi {num} e a sua porção inteira é {inteiro}")

