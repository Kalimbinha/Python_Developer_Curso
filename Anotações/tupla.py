frutas = ("laranja", "pera", "uva",) # colocar virgula no final das tuplas

letras = tuple("python")

numeros = tuple([1,2,3,])

pais = ("Brasil",)  # colocar virgula no final das tuplas

# Exemplo ===========================================================================================================================7

frutas = ("maça","laranja","uva","pera",)

frutas[0] # maça
frutas[2] # uva

frutas[-1] # pera
frutas[-3] # laranja

# Tuplas Aninhadas ======================================================================================================================7

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

tupla = ("p", "y", "t", "h", "o", "n")

tupla[2:] # ["t", "h", "o", "n"]
tupla[:2] # ["p","y"]
tupla[1:3] # ["y","t"]
tupla[0:3:2] # ["p","t"] ultimo valor é o step ou seja o codigo está pulando de 2 em 2 para fazer a checagem 
tupla[::] # ["p", "y", "t", "h", "o", "n"]
tupla[::-1] # ["n", "o", "h", "t", "y", "p"] imprime a tupla ao contrario :o
