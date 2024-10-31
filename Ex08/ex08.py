# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = int(input("Digite o seu metro: "))


km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000




print(f"Metro: {metro}m \nKilometro:{km}km \nHectometro:{hm}hm \nDecametro:{dam}dam \nDecimetro:{dm}dm \nCentímetro:{cm}cm \nMilímetro:{mm}mm")