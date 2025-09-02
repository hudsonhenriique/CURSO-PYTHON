# Faça um programa que receba um núemero.
# VErifique se o número é par ou ímpar.
# Exiba o resultado da seguinte forma:
# "O número X é par" ou "O número X é ímpar"
# %%
def par_ou_impar(numero: int) -> str:
    """Verifica se um número é par ou ímpar.
    numero: int - número a ser verificado."""
    if numero % 2 == 0:
        return f"O número {numero} é par"
    else:
        return f"O número {numero} é ímpar"
# %%
par_ou_impar(10)
# %%
 