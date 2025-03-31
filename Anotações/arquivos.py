# Para ler um arquivo
#file = open('./txt-Eu amo a Isadora.txt','r')
# Para escrever em um arquivo
#file = open('./txt-Eu amo a Isadora.txt','w')
# Para anexar conteúdo a um arquivo existente 
#file = open('./txt-Eu amo a Isadora.txt','a')

file = open('./txt/Eu amo a Isadora.txt','w')
file.write("Amo muito mesmo")
file.close()

file = open('./txt/Eu amo a Isadora.txt','r')
print(file.read())
file.close()

import os
import shutil

# Criar um diretório
os.mkdir("Exemplo")

# Renomear um arquivo
os.rename("Dodo.txt","Isadora.txt")

# Remover um arquivo
os.remove("Dodo.txt")

# Mover um arquivo
shutil.move("Isadora.txt", "txt")