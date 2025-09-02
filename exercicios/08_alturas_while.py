# Faça um programa que leia 4 alturas e realize a soma dessas alturas
# utilizando o laço while.

# %%
soma = 0
contador = 4

while contador > 0:
    altura = float(input("Digite a altura: "))
    soma += altura
    contador -= 1
print(f"A soma das alturas é: {soma:.2f}")
# %%
