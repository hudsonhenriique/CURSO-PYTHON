# %%
import streamlit as st
import requests
import pandas as pd

URL = "https://viacep.com.br/ws/{cep}/json/"
st.title("Consulta de CEP")
cep = st.text_input("Digite o CEP (somente números): ")
if cep != "":
    try:
        response = requests.get(URL.format(cep=cep))
        data = pd.DataFrame([response.json()])
        st.dataframe(data)
    except Exception as err:
        st.error(f"Erro ao consultar o CEP: {err}, tente novamente com um CEP válido.")