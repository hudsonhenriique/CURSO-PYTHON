# %%
def juros_compostos(aporte:int,taxa:float,anos:int)->float:
    """juros compostos serve para calcular o retorno financeiro a partir de um aporte
    Deve-se considerar o valor, a taxa de juros atual e o tempo(em anos) para cálculo do valor a ser retornado.

    Aporte: um número inteiro, que representa o valor em reaios.
    Taxa: um número float entre 0 e 1, que representa a taxa de juros.
    Anos: um número inteiro >=1 que representa o tempo que o invenstimento terá liquidez.
    """
    return  aporte * (1 + taxa) ** anos



# %%
juros_compostos(taxa=0.1,anos=5,aporte=1000)


# %%
