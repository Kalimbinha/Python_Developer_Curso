# Metodos de uma lista --------------------------------------------------------------------------------------------------------------

# [].append

listinha = []

listinha.append(1)
listinha.append("python")
listinha.append([40,30,20])

print(listinha) # [1,"python", [40,30,20]]

# [].clear

listinha = [1,"python", [40,30,20]]

print(listinha) # [1,"python", [40,30,20]]

listinha.clear()

print(listinha) # []

# [].copy

listinha = [1,"python", [40,30,20]]

listinha.copy()

print(listinha) # [1,"python", [40,30,20]]

# [].count

cores = ["vermelho","azul","verde","azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

# [].extend

linguagens = ["python","js","c"]

print(linguagens) # ["python","js","c"]

linguagens.extend("java", "csharp")

print(linguagens) # ["python","js","c","java","csharp"]

# [].index

linguagens = ["python","js","c","java","csharp"]

linguagens.index("java") # 3
linguagens.index("python") # 0

# [].pop 

linguagens = ["python","js","c","java","csharp"]

linguagens.pop() # cshap
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python

# [].remove

linguagens = ["python","js","c","java","csharp"]

linguagens.remove("c")

print(linguagens) # ["python","js","java","csharp"]

# [].reverse

linguagens = ["python","js","c","java","csharp"]

linguagens.reverse()

print(linguagens) # ["csharp", "java","c", "js", "python"]

# [].sort

linguagens = ["python","js","c","java","csharp"]
linguagens.sort() # ordena em ordem alfabetica

linguagens = ["python","js","c","java","csharp"]
linguagens.sort(reverse=True) # ordem alfabetica reversa

linguagens = ["python","js","c","java","csharp"]
linguagens.sort(key=lambda x: len(x)) # ordena por tamanho da string

linguagens = ["python","js","c","java","csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ordena por tamanho da string reversa

# len 

linguagens = ["python","js","c","java","csharp"]

len(linguagens) # 5 (tamanho da lista)

# sorted

linguagens = ["python","js","c","java","csharp"]

sorted(linguagens, key=lambda x: len(x)) # ordena por tamanho da string

sorted(linguagens, key=lambda x: len(x), reverse=True) # ordena por tamanho da string reversa
