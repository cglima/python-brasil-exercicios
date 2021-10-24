""" 
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
valor_hora = float(input("Quanto você recebe por hora? R$ "))
numero_horas_mes = float(input("Quantas horas você trabalha por mês? "))
salario = valor_hora * numero_horas_mes
print(f"O salário a receber é igual a R${salario:.2f}")