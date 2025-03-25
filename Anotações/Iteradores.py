import random

class MeuIterador:
    def __init__(self,numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero + 2
        except IndexError:
            raise StopIteration
        
nu1 = random.randint(1,100)
nu2 = random.randint(1,100)
nu3 = random.randint(1,100)

for i in MeuIterador(numeros=[nu1,nu2,nu3]):
    print(i)