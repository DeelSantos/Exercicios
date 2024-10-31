#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input("Digite o valor do produto: R$"))

desconto = (produto * 5) / 100

novo_valor = produto - desconto

print(f"O novo valor do seu desconto é R${novo_valor:.2f}")



