texto = """
Escolha a garrafa de água que você quer comprar:
(1) Agua Mineral -> R$ 1,50
(2) Agua com Gás -> R$ 2,50
"""
opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.50
    print("Você escolheu Água Mineral - R$ 1,50")
elif opcao == "2":
    valor_item = 2.50
    print("Você escolheu Água com Gás - R$ 2,50")
if valor_item == 0:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
else:
    qtde = input("Quantas garrafas você quer comprar? ")
    valor_total = valor_item * int(qtde)
    print(f"Valor total da compra: R$ {valor_total:.2f}")