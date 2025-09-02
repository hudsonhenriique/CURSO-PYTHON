# Escreva um programa que receba uma lista de números do usuário e
# conte quantas vezes cada número aparece na lista.
# Solicite ao um nuero e exiba contagem
# %%
lista = [1,2,3,3,2,1,1,1,1,1,1,5,6,7,7,6,5,4,3,2,1]

num = int(input("Digite um número para saber quantas vezes ele aparece na lista: "))

contador = 0
for i in lista:
    if i == num:
        contador += 1
print(f"O número {num} aparece {contador} vezes na lista.")
# %%
