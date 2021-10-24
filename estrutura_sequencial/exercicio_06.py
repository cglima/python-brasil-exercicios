""" 
6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
from math import pi

raio_circulo = float(input("Digite o raio do círculo: "))
area_circulo = pi * (raio_circulo ** 2)
print(f"A área do círculo é: {area_circulo:.2f} m2")