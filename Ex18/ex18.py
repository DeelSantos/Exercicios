#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input("Digite seu ângulo: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"Seu ângulo mede {angulo:.1f}\nSeu seno é {seno}\nSeu cosseno é {cosseno}\nSua tangente é {tangente}")