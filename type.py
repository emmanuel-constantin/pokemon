from pokemon import *

class Type(Pokemon):
    def __init__(self):
        Pokemon.__init__(self)
        self.typepokemonchoisi = ""  
    def typepokemon(self):
        if self.pokemonchoisi == "Salameche":
            self.typepokemonchoisi = "Feu"
            self.listepokemon.pop(0)
        elif self.pokemonchoisi == "Carapuce":
            self.typepokemonchoisi = "Eau"
            self.listepokemon.pop(1)
        elif self.pokemonchoisi == "Rattata":
            self.typepokemonchoisi = "Normal"
            self.listepokemon.pop(2)
        elif self.pokemonchoisi == "Taupiqueur":
            self.typepokemonchoisi = "Terre"
            self.listepokemon.pop(3)
        else:
            print("Le nom de pokemon entré n'est pas valide")
    def changementinfospokemontype(self):
        if self.typepokemonchoisi == "Feu":
            Pokemon.setPV(self,90)
            self.pattaque = 50
            self.defense = 10
        if self.typepokemonchoisi == "Eau":
            Pokemon.setPV(self,110)
            self.pattaque = 30
            self.defense = 20
        if self.typepokemonchoisi == "Normal":
            Pokemon.setPV(self,120)
            self.pattaque = 40
            self.defense = 30
        if self.typepokemonchoisi == "Terre":
            Pokemon.setPV(self,130)
            self.pattaque = 20
            self.defense = 40

            
            
            

