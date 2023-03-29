from pokemon import *
from type import *


class Combat(Type):
    def __init__(self, pokemon1, pokemon2):
        Type.__init__(self)
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.vainqueur = ""
    def verifie(self):
        if self.getPV(self.pokemon1) == 0:
            self.vainqueur = "Joueur"
        elif self.getPV(self.pokemon2) == 0:
            self.vainqueur = "Adversaire"
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
    def attaque(self):
        if self.pokemon1 == "Salameche":
            if self.pokemon2 == "Salameche":
                self.pattaque = self.pattaque
            if self.pokemon2 == "Carapuce":
                self.pattaque = self.pattaque*0.5
            if self.pokemon2 == "Rattata":
                self.pattaque = self.pattaque
            if self.pokemon2 == "Taupiqueur":
                self.pattaque = self.pattaque*2
        if self.pokemon1 == "Carapuce":
            if self.pokemon2 == "Salameche":
                self.pattaque = self.pattaque*2
            if self.pokemon2 == "Carapuce":
                self.pattaque = self.pattaque
            if self.pokemon2 == "Rattata":
                self.pattaque = self.pattaque
            if self.pokemon2 == "Taupiqueur":
                self.pattaque = self.pattaque*0.5
        if self.pokemon1 == "Rattata":
            if self.pokemon2 == "Salameche":
                self.pattaque = self.pattaque*0.75
            if self.pokemon2 == "Carapuce":
                self.pattaque = self.pattaque*0.75
            if self.pokemon2 == "Rattata":
                self.pattaque = self.pattaque
            if self.pokemon2 == "Taupiqueur":
                self.pattaque = self.pattaque*0.75
        if self.pokemon1 == "Taupiqueur":
            if self.pokemon2 == "Salameche":
                self.pattaque = self.pattaque*0.5
            if self.pokemon2 == "Carapuce":
                self.pattaque = self.pattaque*2
            if self.pokemon2 == "Rattata":
                self.pattaque = self.pattaque
            if self.pokemon2 == "Taupiqueur":
                self.pattaque = self.pattaque      
    # def defensePV(self)