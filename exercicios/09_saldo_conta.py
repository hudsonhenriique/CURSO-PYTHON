# Faça um programa que receba uma quantidade indefinida de valores
# corerspondentes a "saldo de uma conta",
# mas quando o usuário apertar "enter" sem digitar nada,
# o programa para de receber valores, e exibe a soma
# de todos os valores digitados antorioramente.

saldo_total = 0

while True:
    saldo = input("Digite o saldo da conta (ou pressione Enter para sair): ")
    if saldo == "":
        break
    saldo_total += float(saldo)
print(f"Soma total dos saldos: {saldo_total:.2f}")
