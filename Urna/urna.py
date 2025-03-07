import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  

def main():
    limpar_terminal()
    caixaDeTexto("Bem-vindo ao sistema da Urna Eletrônica")
    senha = cadastrar()
    confirmarSenha(senha)
    urna()

def cadastrar():
    while True:
        senha = input("Defina a sua senha: ")
        conf = input("Confirme a sua senha: ")
        limpar_terminal()

        if senha == conf:
            caixaDeTexto("Sua senha foi cadastrada com sucesso :)")
            return senha  
        else:
            print("As senhas não coincidem. Tente novamente.")

def confirmarSenha(senha):
    while True:
        conf = input("Digite sua senha para acessar a Urna: ")

        if conf == senha:
            print("Senha confirmada com sucesso!")
            break
        else:
            print("Senha incorreta. Tente novamente.")

def urna():
    limpar_terminal()
    caixaDeTexto("Bem-vindo à Urna Eletrônica")
    caixaDeTexto("O que você deseja fazer?")
    
    print("1 - Iniciar votação")
    print("2 - Encerrar a votação")
    op = input("-> ")

    if op == "1":
        votacao()
    if op == "2":
        exit()

def votacao():
    limpar_terminal()

    dadosGerais = [
        ("Pedro", 0),
        ("Isadora", 0),
        ("Fernando", 0),
        ("Kalimbinha", 0),
        ("Branco", 0),
        ("Nulos", 0)
    ]

    votos = dict(dadosGerais)
    
    while True:
        imprimir_tabela(votos)

        try:
            voto = input("Digite o número do candidato para votar ou 'sair' para terminar: ").strip()

            if voto == 'sair':
                break

            voto_numero = int(voto)  
            if voto_numero < 1 or voto_numero > len(votos):
                print("Número inválido! Tente novamente.")
            else:
                candidato = list(votos.keys())[voto_numero - 1]  
                votos[candidato] += 1  
                print(f"Voto registrado para {candidato}!")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número de candidato.")

    print("\nResultado final dos votos:")
    for candidato, numero_votos in votos.items():
        print(f"{candidato}: {numero_votos} votos")
    
    candidatos_com_mais_votos = sorted(votos.items(), key=lambda x: x[1], reverse=True)
    if candidatos_com_mais_votos[0][1] == candidatos_com_mais_votos[1][1]:
        print("\nHouve um empate entre os dois candidatos mais votados!")
        segundo_turno(candidatos_com_mais_votos)
    else:
        print("\nNão houve empate, o vencedor foi:", candidatos_com_mais_votos[0][0])

def segundo_turno(candidatos):
    
    limpar_terminal()
    caixaDeTexto("Iniciando o Segundo Turno")
    caixaDeTexto("Escolha entre os dois candidatos mais votados:")
    
    print("1 -", candidatos[0][0])
    print("2 -", candidatos[1][0])

    votos_segundo_turno = {candidatos[0][0]: 0, candidatos[1][0]: 0}

    while True:
        try:
            voto = input(f"Digite o número do candidato para votar ou 'sair' para terminar o segundo turno: ").strip()

            if voto == 'sair':
                break

            voto_numero = int(voto)  
            if voto_numero == 1:
                votos_segundo_turno[candidatos[0][0]] += 1
                print(f"Voto registrado para {candidatos[0][0]}!")
            elif voto_numero == 2:
                votos_segundo_turno[candidatos[1][0]] += 1
                print(f"Voto registrado para {candidatos[1][0]}!")
            else:
                print("Número inválido! Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número de candidato.")
            limpar_terminal()
            
    print("\nResultado final do segundo turno:")
    for candidato, numero_votos in votos_segundo_turno.items():
        print(f"{candidato}: {numero_votos} votos")
    
    vencedor = max(votos_segundo_turno, key=votos_segundo_turno.get)
    print(f"\nO vencedor do segundo turno é {vencedor}!")

def caixaDeTexto(texto):
    largura = len(texto) + 2
    print("+" + "=" * largura + "+")
    print("| " + texto + " |")
    print("+" + "=" * largura + "+")

def imprimir_tabela(votos):
    largura_numero = 5
    largura_nome = max(len(nome) for nome, _ in votos.items()) + 2
    largura_votos = 5

    print("+" + "=" * (largura_numero + largura_nome + largura_votos + 7) + "+")
    print(f"| {'Numero'.ljust(largura_numero)} | {'Candidatos'.ljust(largura_nome)}| {'Votos'.ljust(largura_votos)}|")
    print("+" + "=" * (largura_numero + largura_nome + largura_votos + 7) + "+")

    for index, (nome, numero) in enumerate(votos.items(), 1):
        print(f"| {str(index).ljust(largura_numero)} | {nome.ljust(largura_nome)} |{str(numero).center(largura_votos)} |")

    print("+" + "=" * (largura_numero + largura_nome + largura_votos + 7) + "+")

# Chama a função principal
if __name__ == "__main__":
    main()
