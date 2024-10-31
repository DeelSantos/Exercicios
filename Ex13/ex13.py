#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite seu salário: R$"))

acrescimo = (salario * 15) / 100

novo_salario = salario + acrescimo

print(f"Parabéns, seu novo salário é de {novo_salario:.2f}")




