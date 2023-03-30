class Pokemon:
    def __init__(self):
        self.__pv = 100
        self.original_attaque = 0
        self.defense = 0
        self.pokemonchoisi = ""
    def choisirpokemon(self):
        self.pokemonchoisi = input("Choisissez un pokemon parmi ces 4 : Salameche (feu), Carapuce (eau), Rattata (normal), Taupiqueur (terre): ")
    def afficherInfosPokemon(self):
        print("Nom du pokemon :", self.pokemonchoisi)
        print("PV =", self.__pv)
        print("Attaque =", self.original_attaque)
        print("Defense =", self.defense)

    def setpAttaque(self, pa):
        self.pattaque = pa
    def setPV(self, pointsdevie):
        self.__pv = pointsdevie

    def getNomPokemon(self):
        return self.pokemonchoisi
   
    def getPV(self):
        return self.__pv