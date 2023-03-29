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

combat1 = Combat(pokemon1, adversaire1)
combat1.verifie()
combat1.attaque()
pokemon1.getpAttaque()
# combat1.defense()





# while True:
#     input("")
