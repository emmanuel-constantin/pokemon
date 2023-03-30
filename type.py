from pokemon import *

class Type(Pokemon):
    
    def __init__(self):
        Pokemon.__init__(self)
        self.typepokemonchoisi = ""
   
    def typepokemon(self):
        if self.pokemonchoisi == "Salameche":
            self.typepokemonchoisi = "Feu"
        elif self.pokemonchoisi == "Carapuce":
            self.typepokemonchoisi = "Eau"
        elif self.pokemonchoisi == "Rattata":
            self.typepokemonchoisi = "Normal"
        elif self.pokemonchoisi == "Taupiqueur":
            self.typepokemonchoisi = "Terre"
        else:
            print("Le nom de pokemon entré n'est pas valide")
        return self.typepokemonchoisi
   
    def changementinfospokemontype(self):
        self.typepokemon()
        if self.typepokemonchoisi == "Feu":
            Pokemon.setPV(self,90)
            self.original_attaque = 50
            self.defense = 10
        
        if self.typepokemonchoisi == "Eau":
            Pokemon.setPV(self,110)
            self.original_attaque = 30
            self.defense = 20
        
        if self.typepokemonchoisi == "Normal":
            Pokemon.setPV(self,120)
            self.original_attaque = 40
            self.defense = 30
       
        if self.typepokemonchoisi == "Terre":
            Pokemon.setPV(self,130)
            self.original_attaque = 20
            self.defense = 40
    def getType(self):
        return self.typepokemonchoisi
    
    def getpAttaque(self):
        attaque = self.pattaque
        return attaque
    
    def getDefense(self):
        defense = self.defense
        return defense
            
            
            

