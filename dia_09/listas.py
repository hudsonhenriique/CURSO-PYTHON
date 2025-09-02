# %%
# Primeira forma de criar uma lista
x =[]
for i in range(1,101):
     x.append(i)
x
# %%
# Segunda forma de criar uma lista (List Comprehension)
y = [i for i in range(1,101)]
y
# %%
# Terceira forma de criar uma lista (List Comprehension com condição)
def eh_par(n):
    return n % 2 == 0
pares = [i for i in range(1,101) if eh_par(i)]
pares
# %%
