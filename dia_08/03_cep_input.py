# %%
import requests

cep = input("Digite o CEP (somente números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url.format(cep=cep))

if response.status_code == 200:
    data = response.json()
    if "erro" not in data:
        print(f"CEP: {data['cep']}")
        print(f"Logradouro: {data['logradouro']}")
        print(f"Bairro: {data['bairro']}")
        print(f"Cidade: {data['localidade']}")
        print(f"Estado: {data['uf']}")
    else:
        print("CEP não encontrado.")
# %%
