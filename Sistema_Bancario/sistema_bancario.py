from datetime import datetime

def exibir_menu():
    return """\n
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==========================
    => """

def registrar_transacao(extrato, tipo, valor):
    """Adiciona uma transação ao extrato com data e hora."""
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato.append(f"[{data_hora}] {tipo}: R$ {valor:.2f}")

def depositar(saldo, extrato, valor, num_transacoes, LIMITE_TRANSACOES):
    if num_transacoes >= LIMITE_TRANSACOES:
        print("\nErro! Limite diário de transações atingido.")
    elif valor > 0:
        saldo += valor
        registrar_transacao(extrato, "Depósito", valor)
        num_transacoes += 1
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nErro! O valor do depósito deve ser positivo.")
    return saldo, extrato, num_transacoes

def sacar(saldo, extrato, valor, num_saques, limite, LIMITE_SAQUES, num_transacoes, LIMITE_TRANSACOES):
    if num_transacoes >= LIMITE_TRANSACOES:
        print("\nErro! Limite diário de transações atingido.")
    elif valor > saldo:
        print("\nErro! Saldo insuficiente.")
    elif valor > limite:
        print("\nErro! O saque excede o limite permitido.")
    elif num_saques >= LIMITE_SAQUES:
        print("\nErro! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        registrar_transacao(extrato, "Saque", valor)
        num_saques += 1
        num_transacoes += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nErro! O valor do saque deve ser positivo.")
    
    return saldo, extrato, num_saques, num_transacoes

def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print("=============================")

def main():
    saldo = 0
    limite = 500
    extrato = []
    num_saques = 0  
    LIMITE_SAQUES = 3
    num_transacoes = 0  
    LIMITE_TRANSACOES = 10  # Novo limite de transações diárias

    while True:
        opcao = input(exibir_menu()).strip().lower()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato, num_transacoes = depositar(saldo, extrato, valor, num_transacoes, LIMITE_TRANSACOES)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, num_saques, num_transacoes = sacar(saldo, extrato, valor, num_saques, limite, LIMITE_SAQUES, num_transacoes, LIMITE_TRANSACOES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("\nObrigado por usar nosso sistema bancário! Até mais! 😊")
            break

        else:
            print("\nOperação inválida! Escolha uma opção do menu.")

# Executar o programa
if __name__ == "__main__":
    main()
