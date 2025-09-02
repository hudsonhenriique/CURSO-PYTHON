# Escreva um programa que solicite ao usuário frases
# para parar de solicitar frases, ele pode apertar o enter
# o programa deve apresentar cada frase e quantas vezes ela foi repetida

dados = {}
while True:
    frase = input("Digite uma frase (ou pressione Enter para sair): ")
    if frase == "":
        break
    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1
for frase, contagem in dados.items():
    
    print(f'A frase "{frase}" foi repetida {contagem} vezes.')