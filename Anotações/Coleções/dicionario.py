# Dicionario =================================================================================================================================

pessoa = {"nome":"Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3333-1234" # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"] # "Guilherme"
dados["idade"] # 28
dados["telefone"] # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

dados # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

contatos = {
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"},
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"},
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"},
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"},
}

contatos["fernando@gmail.com"]["telefone"]

for chave in contatos:
    print(chave, contatos[chave])
    
for chave, valor in contatos.items():
    print(chave,valor)
    
    # "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"}
    # "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"}
    # "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"}
    # "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"}

# Metodos =================================================================================================================================

# {}.clear

contatos = {
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"},
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"},
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"},
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"},
}

contatos.clear()
contatos # {}

# {}.copy

contatos = {
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"] # {"nome": "Guilherme", "telefone": "3333-2221"}

copia["guilherme@gmail.com"] # {"nome": "Gui"}

# {}.fromkeys

dict.fromkeys(["nome","telefone"]) # {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"],"vazio") # {"nome": vazio, "telefone": vazio}

# {}.get

contatos = {
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"}
}

contatos["chave"] # KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {}) # {"nome": "Guilherme", "telefone": "3333-2221"}

# {}.items

contatos = {
    "fernando@gmail.com": {"nome": "fernando", "telefone": "3333-1231"}
}

contato.items() # dict_items([('fernando@gmail.com',{'nome': 'Fernando','telefone': '3333-2221'})])