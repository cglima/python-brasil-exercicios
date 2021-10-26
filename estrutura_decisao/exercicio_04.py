"""
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input("Digite uma letra: ").lower()
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("1 - A letra digitada é uma vogal")
else:
    print("1 - A letra digitada é uma consoante")

vogais = "aeiou"
if letra in vogais:
    print("2 - A letra digitada é uma vogal")
else:
    print("2 - A letra digitada é uma consoante")

vogais = ["a", "e", "i", "o", "u"]
if letra in vogais:
    print("3 - A letra digitada é uma vogal")
else:
    print("3 - A letra digitada é uma consoante")
