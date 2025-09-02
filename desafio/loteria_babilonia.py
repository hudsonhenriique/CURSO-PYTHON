# Construa um programa que realiza um sorteiro de um número entre 1 e 15.
# O usuário tem 3 tentativas para acertar o número sorteado.
# A cada tentativa, o programa deve informar se o número digitado é maior ou menor que o número sorteado.
# Se o usuário acertar o número, o programa deve parabenizá-lo e encerrar.
# Se o usuário não acertar em 3 tentativas, o programa deve revelar o número sorteado.
import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("Digite um número entre 1 e 15: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue
        if 1 <= numero_usuario <=15:
            print(f"Você tem {2 - i} tentativas restantes.")
            return numero_usuario
        print("Número fora do intervalo. Tente novamente.")
        
numero_sorteio = random.randint(1, 15)

for i in range(3):

    numero_usuario = get_input()
    
    if numero_usuario == numero_sorteio:
                print("Parabéns! Você acertou o número!")
                break
    elif numero_usuario < numero_sorteio:
                print("O número digitado é menor que o número sorteado.")
    else:
                print("O número digitado é maior que o número sorteado.")
    
else:
    print(f"Suas tentativas acabaram. O número sorteado era {numero_sorteio}.")

