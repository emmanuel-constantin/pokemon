from pokemon import *
from type import *


class Combat(Type):
    def __init__(self, pokemon1, pokemon2):
        Type.__init__(self)
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.vainqueur = ""
         
    def verifie(self):
        if self.pokemon1.getPV() <= 0:
            self.vainqueurcombat = "Adversaire"
        else:
            self.vainqueurcombat = "Joueur"
        return self.vainqueur
    
    def vainqueur(self):
        if self.vainqueur == "Joueur":
            print("Le vainqueur est le joueur !")
        if self.vainqueur == "Adversaire":
            print("L'adversaire a gagné ! ")
    
    def perdant(self):
        if self.vainqueur == "Joueur":
            print(self.pokemon2,"a perdu")
        if self.vainqueur == "Adversaire":
            print(self.pokemon1,"a perdu")
    
    def puissance_attaque(self):
        type_pokemon1 = self.pokemon1.getType()
        type_pokemon2 = self.pokemon2.getType()
        attaque = self.pokemon1.original_attaque

        if type_pokemon1 == "Feu":
            if type_pokemon2 == "Eau":
                attaque *= 0.5
            elif type_pokemon2 == "Terre":
                attaque *= 2

        elif type_pokemon1 == "Eau":
            if type_pokemon2 == "Feu":
                attaque *= 2
            elif type_pokemon2 == "Terre":
                attaque *= 0.5

        elif type_pokemon1 == "Terre":
            if type_pokemon2 == "Feu":
                attaque *= 0.5
            elif type_pokemon2 == "Eau":
                attaque *= 2
        self.pokemon1.setpAttaque(attaque)
        return attaque

    def defensepokemon(self):
        self.attaquepokemon1 = self.puissance_attaque()
        self.pvpokemonquidef = self.pokemon2.getPV()
        self.defpokemon = self.pokemon2.getDefense()
        attaque_rest = self.pvpokemonquidef - (self.attaquepokemon1 - self.defpokemon)
        self.pokemon2.setPV(attaque_rest)
        print("Il reste", self.pokemon2.getPV(), "PV à", self.pokemon2.getNomPokemon())