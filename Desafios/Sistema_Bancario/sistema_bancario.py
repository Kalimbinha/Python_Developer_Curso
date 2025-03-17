from datetime import datetime

# Listas para armazenar usuários e contas
usuarios = []
contas = []
AGENCIA = "0001"

def exibir_menu():
    return """\n
    ========== MENU ==========
    [u] Criar Usuário
    [c] Criar Conta Bancária
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==========================
    => """

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ").strip()
    usuario_existente = next((user for user in usuarios if user["cpf"] == cpf), None)

    if usuario_existente:
        print("\nErro! Já existe um usuário com esse CPF.")
        return
    
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ").strip()
    endereco = input("Informe o endereço (Rua, Número - Bairro - Cidade/Estado): ").strip()

    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("\nUsuário cadastrado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do titular da conta: ").strip()
    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)

    if not usuario:
        print("\nErro! Usuário não encontrado. Cadastre um usuário primeiro.")
        return
    
    numero_conta = len(contas) + 1
    contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
    print(f"\nConta criada com sucesso! Agência: {AGENCIA} | Conta: {numero_conta}")

def registrar_transacao(extrato, tipo, valor):
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

def selecionar_conta():
    cpf = input("Informe o CPF do titular da conta: ").strip()
    contas_usuario = [conta for conta in contas if conta["usuario"]["cpf"] == cpf]

    if not contas_usuario:
        print("\nErro! Nenhuma conta encontrada para esse CPF.")
        return None

    print("\nContas disponíveis:")
    for conta in contas_usuario:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']}")

    numero_conta = int(input("\nInforme o número da conta desejada: "))
    conta_selecionada = next((conta for conta in contas_usuario if conta["numero_conta"] == numero_conta), None)

    if not conta_selecionada:
        print("\nErro! Conta inválida.")
        return None

    return conta_selecionada

def main():
    saldo = 0
    limite = 500
    extrato = []
    num_saques = 0  
    LIMITE_SAQUES = 3
    num_transacoes = 0  
    LIMITE_TRANSACOES = 10  

    while True:
        opcao = input(exibir_menu()).strip().lower()

        if opcao == "u":
            criar_usuario()

        elif opcao == "c":
            criar_conta()

        elif opcao in ["d", "s", "e"]:
            conta = selecionar_conta()
            if not conta:
                continue

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

if __name__ == "__main__":
    main()
