# Faça um programa que leia 4 alturas e realize a soma dessas alturas
# utilizando o laço for.
# %%
soma_alturas = 0
for i in range(4):
    altura = float(input(f"Digite a altura {i + 1}: "))
    soma_alturas += altura
print(f"A soma das alturas é: {soma_alturas:.2f}")
# %%
