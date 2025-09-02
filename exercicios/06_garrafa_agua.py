texto = """
Escolha a garrafa de água que você quer comprar:
(1) Agua Mineral -> R$ 1,50
(2) Agua com Gás -> R$ 2,50
"""
opcao = input(texto)

if opcao == "1":
    print("Você escolheu Água Mineral - R$ 1,50")
elif opcao == "2":
    print("Você escolheu Água com Gás - R$ 2,50")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")