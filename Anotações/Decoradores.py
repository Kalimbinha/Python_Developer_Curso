def mensagem(nome):
    print("Executando a funcao")
    return f"Ola {nome}"

def mensagem_longa(nome):
    print("Executando a funcao longa")
    return f"Ola tudo bem com você {nome}?"

def executar(funcao,nome):
    print("Executando a funcao executar")
    return funcao(nome)


print(executar(mensagem, "Fernando"))
print(executar(mensagem_longa, "Isadora"))