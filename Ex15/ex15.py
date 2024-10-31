#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Quantos dias de aluguel? "))
km_rodado = int(input("Quantos KM rodados? "))

preco_dia = dias * 60
preco_km = km_rodado * 0.15

total_pagamento = preco_dia + preco_km

print(f"O preço pelos dias foi de R${preco_dia:.2f}\nO preço pelos km foi {preco_km:.2f}km.\nO total a pagar é R${total_pagamento:.2f}")