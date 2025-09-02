# %%
def soma(a:float,b:float,*args) -> float:
    valores = [a,b] + list(args)
    return sum(valores)
# %%

def media(a:float,b:float,*args) -> float:
    return soma(a,b,*args) / (len(args)+2)
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

print("Média:",media(a,b))
# %%
