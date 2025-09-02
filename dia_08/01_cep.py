# %%
import requests # para fazer requisições HTTP
import json # para manipular dados em JSON
from tqdm import tqdm # para mostrar barra de progresso
import pandas as pd # para manipulação de dados
# %%
ceps = ["30110010",
        "30130141",
        "30140072",
        "30150221",
        "30170130",
        "30240520",
        "30310470",
        "30380090",
        "30411127",
        "30535530",
        "30575180",
        "31035560",
        "31140540",
        "31270330",
        "31741400",
        ]

url = "https://viacep.com.br/ws/{cep}/json/"
dados =[]
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
            dados.append(resposta.json())
dados

# %%
dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", index=False, encoding="utf-8", sep=";")
# %%
with open("ceps.json", "w",encoding="utf-8") as open_file:
    json.dump(dados, open_file, indent=4, ensure_ascii=False)


# %%
