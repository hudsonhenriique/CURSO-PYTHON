# %%
nome_arquivo =  'historia.txt'

with open(nome_arquivo, 'r', encoding='utf-8') as open_file:
    conteudo = open_file.read()

print(conteudo)





# open_file = open(nome_arquivo, 'r', encoding='utf-8')
# # %%
# conteudo = open_file.read()
# print(conteudo)
# # %%
# open_file.close()
# %%
