#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input("Digite a sua tabuada: "))

print(f"Tabuada do {numero}")

for i in range(0, 11):
    print(f"{numero} x {i}:", numero * i)
    
    
    
    