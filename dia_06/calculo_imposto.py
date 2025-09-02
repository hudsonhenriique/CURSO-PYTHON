# %%
def calc_imposto(preco:float,tx_base:float,**kwargs):
    imposto = preco * tx_base
    for i in kwargs:
        print(i,kwargs[i])
        imposto += preco * kwargs[i]
    return imposto
# %%
impostos_gerais = {
    'municipal':0.01,
    'estadual':0.03,
    'federal':0.05
}
calc_imposto(100,0.02,**impostos_gerais)
# %%
calc_imposto(100,0.02,municipal=0.01,estadual=0.03,federal=0.05)
# %%
