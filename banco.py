menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""
saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Inforte o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor}\n"
        else:
            print("Operação falhou, Digite novamente")

    elif opcao == "s":
        valor = float(input("Inforte o valor do saque: "))

        excedeu_saldo = valor > saldo

        saldo_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, digite um saldo sufience")

        elif saldo:
            print("Operação falhou, o saque excedeu o limite")

        elif excedeu_saques:
            print("Operação falhou, o numero de saques excedeu o limite")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor}\n"
            numero_saques += 1

        else:
            print("Operação falhou, digite novamente")

    elif opcao == "e":
        print("\n =================== EXTRATO ===================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\n Saldo de {saldo}")
        print("=====================================")

    elif opcao == "q":
        break

    else:
        print("Movimentação invalida, faça novamente")
