# %%
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"
response = requests.get(url)
df = pd.DataFrame(response.json())
# %%
df.to_csv("heroes.csv", index=False, encoding="utf-8",sep=";")


# %%
