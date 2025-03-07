# lista ---------------------------------------------------------------------------------------------------------------------------
frutas = ["laranja","marca","uva"]

patos = []

letras = list("python")

numeros = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]

# Para escolher um valor em python precisamos pegar por valores de array

frutas[-1] # uva

frutas[1] #laranja

# Exemplo

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p","y"]
lista[1:3] # ["y","t"]
lista[0:3:2] # ["p","t"] ultimo valor é o step ou seja o codigo está pulando de 2 em 2 para fazer a checagem 
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"] imprime a lista ao contrario :o

# Filtro versão 1

numero = [1,30,21,2,9,65,34]
pares = []

for nuemro in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Filtro versão 1

numero = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0] # for em uma linha

# Modificando valores vesão 1

numero = [1,30,21,2,9,65,34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# Modificando valores vesão 2

numero = [1,30,21,2,9,65,34]
quadrado = [numero ** 2 for numero in numeros]




