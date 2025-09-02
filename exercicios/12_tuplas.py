#Escreva um programa que crie um dicionario
#Com nomes de frutas como chaves e suas respectivas preços como valores.
#Solicite ao ususario o nome de uma fruta e exiba o preço correspondente.
frutas = {}

while True:
    print("\nMenu:")
    print("1 - Adicionar fruta")
    print("2 - Buscar preço de uma fruta")
    print("3 - Listar todas as frutas")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome da fruta: ")
        preco = float(input(f"Digite o preço de {nome}: "))
        frutas[nome] = preco
        print(f"{nome} adicionada com sucesso!")
    elif opcao == '2':
        nome_busca = input("Digite o nome da fruta para buscar o preço: ")
        if nome_busca in frutas:
            print(f"O preço de {nome_busca} é R$ {frutas[nome_busca]:.2f}")
        else:
            print(f"{nome_busca} não encontrada no dicionário.")
    elif opcao == '3':
        print("Frutas cadastradas:")
        for fruta, preco in frutas.items():
            print(f"{fruta}: R$ {preco:.2f}")
    elif opcao == '4':
        print("Encerrando o programa. Frutas cadastradas:")
        for fruta, preco in frutas.items():
            print(f"{fruta}: R$ {preco:.2f}")
        break
    else:
        print("Opção inválida. Tente novamente.")


