class Animal():
    def __init__(self,peso,cor):
        self.peso = peso
        self.cor = cor
        

    def fala(self):
        return "falando de forma GENERICA"

class Cachorro(Animal):
    def __init__(self,peso,cor):
        Animal.__init__(self,peso,cor)
    
    def fala(self):
        return f"Au !! {self.peso},{self.cor}"

class Gato(Animal):
    def __init__(self,peso,cor):
        Animal.__init__(self,peso,cor)

    def fala(self):
        return f"Miau {self.peso},{self.cor}"

class Pato(Animal):
    def __init__(self,peso,cor):
         Animal.__init__(self,peso,cor)

    def fala(self):
        return f"Quack {self.peso},{self.cor}"

lista = [Cachorro(20,"Preto"),Gato(15,"branco"),Pato(10,"vermelha")]
for animal in lista:
    print(animal.fala())

'''orientação a Obejetos
Aula 09 LP2
'''