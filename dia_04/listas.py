# %%

idades = [39, 30, 27, 18, 9, 6, 3, 10]

print(idades[2])

print("Soma das idades:", sum(idades))
print("Média das idades:", sum(idades)/len(idades))
print("Maior idade:", max(idades))
print("Menor idade:", min(idades))
# %%
Hudson = ["Hudson", 
          33,
          1.83,
          "Masculino",
          "Casado",
          ["Ageville","Professor","Programador"],
          [1800,2500,4000],
          ["Python","Java","JavaScript"]]

print("Tamanho da lista:", len(Hudson))
Hudson.append("Brasileiro")
print("Tamanho da lista após append:", len(Hudson))
print(Hudson[-1])
print(Hudson[-2][0])
   # %%
print(Hudson[0:5])
print(Hudson[5][1:3])
print(Hudson[5][-2:])
print(Hudson[:4])

salarios = Hudson[6]
salarios[::-1]

# )%%

# %%
