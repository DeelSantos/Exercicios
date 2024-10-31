#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.


dinheiro = float(input("Digite o quanto você tem na carteira? R$"))
dolar = float(input("Digite o valor do dólar: "))


dinheiro_em_dolar = dinheiro / dolar

print(f"Se você trocar seu dinheiro para dólar, você terá ${dinheiro_em_dolar:.2f}")