# %%
idades = []

while True:
    idade = int(input("Digite uma idade (ou -1 para sair): "))
    if idade == -1:
        break
    idades.append(idade)
media = sum(idades)/len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)
print(idades)
print(f"Média: {media}, Mínimo: {minimo}, Máximo: {maximo}, Quantidade: {qtde}")
# %%
