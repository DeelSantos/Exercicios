#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = int(input("Digite o grau atual: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"O graus em Fahrenheit é: {fahrenheit}ºF")