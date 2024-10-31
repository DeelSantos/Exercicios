# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Digite a largura da sua parede: "))
altura = float(input("Digite a altura da sua parede: "))

area = largura * altura

tinta =  area / 2

print(f"Sua parede tem {largura} de largura e {altura} de altura.\nA área da sua parede é {area}\n Você vai precisar de {tinta} litros de tinta para pintar a mesma")