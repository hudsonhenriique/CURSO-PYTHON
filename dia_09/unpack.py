# %%
A = 1
B = 5
print(A)
print(B)
# %%
C = A
A = B
B = C
print(A)
print(B)
# %%
A, B = B, A
print(A)
print(B)
# %%
a,b,*rest = 1,2,3,4,5,6,7,8,9
print(a,b,rest)
# %%
a,b, *_ = 1,2,3,4,5,6,7,8,9
print(a,b)
# %%
a, b, *_, c = 1,2,3,4,5,6,7,8,9
print(a,b,c)
# %%
a,*_,b = 1,2,3,4,5,6,7,8,9
print(a,b,_)
# %%
def soma(a,*args):
    total = a + sum(args)
    return total
soma(1,2,3)
# %%
dados = {
    'nome': 'João',
    'idade': 30,
    }
for i,j in dados.items():
    print(i, j)
# %%
