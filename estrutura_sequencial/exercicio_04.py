""" 
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
nota1 = int(input("Digite a primeira nota do bimestre: "))
nota2 = int(input("Digite a segunda nota do bimestre: "))
nota3 = int(input("Digite a terceira nota do bimestre: "))
nota4 = int(input("Digite a quarta nota do bimestre: "))

media = (nota1 + nota2 + nota3 + nota4)/ 4
# media = soma/4
print(f"A média das notas bimestrais é igual a {media}")
