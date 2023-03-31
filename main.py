from pokemon import *
from type import *
from combat import *

pokemon1 = Type()
pokemon1.choisirpokemon()
pokemon1.typepokemon()
pokemon1.changementinfospokemontype()
pokemon1.afficherInfosPokemon()

print()
print("Tour de l'adversaire : ")
print()

adversaire1 = Type()
adversaire1.choisirpokemon()
adversaire1.typepokemon()
adversaire1.changementinfospokemontype()
adversaire1.afficherInfosPokemon()

print()

combat1 = Combat(pokemon1, adversaire1)
fin_combat = False
tour = 1


fin_combat = False
tour = 1
while not fin_combat:
    if tour == 1:
        combat1.pokemon1 = pokemon1
        combat1.pokemon2 = adversaire1
    else:
        combat1.pokemon1 = adversaire1
        combat1.pokemon2 = pokemon1
    combat1.puissance_attaque()
    print("L'attaque de", combat1.pokemon1.getNomPokemon(), "est de", combat1.pokemon1.getpAttaque(), "contre", combat1.pokemon2.getNomPokemon(),"qui a une défense de", combat1.pokemon2.getDefense())
    combat1.defensepokemon()
    if pokemon1.getPV() <= 0:
        print("Le joueur 2 a gagné")
        fin_combat = True
    elif adversaire1.getPV() <= 0:
        print("Le joueur 1 a gagné")
        fin_combat = True
    tour = -tour




