# %%
dados_Hudson = {
    "nome": "Hudson",
    "idade": 33,
    "altura": 1.83,
    "pais": "Brasil",
    "profissao": "Dados Junior",
    "linguagens": ["Python", "R", "SQL"],
     "filho":True
}

dados_Hudson["linguagens"][0]
dados_Hudson["estado civil"] = "Casado"
print(dados_Hudson)
dados_Hudson.keys()
print(dados_Hudson.values())
# %%
for i in dados_Hudson:
    print(i, "->", dados_Hudson[i])
# %%
for chave, valor in dados_Hudson.items():
    print(chave, "->", valor)
# %%
