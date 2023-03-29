class Pokemon:
    def __init__(self):
        self.__pv = 100
        self.pattaque = 0
        self.defense = 0
        self.listepokemon = ["Salameche", "Carapuce", "Rattata", "Taupiqueur"]
    def choisirpokemon(self):
        self.pokemonchoisi = input("Choisissez un pokemon parmi ces 4 : Salameche (feu), Carapuce (eau), Rattata (normal), Taupiqueur (terre): ")
    def afficherInfosPokemon(self):
        print("Nom du pokemon :", self.pokemonchoisi)
        print("PV =", self.__pv)
        print("Attaque =", self.pattaque)
        print("Defense =", self.defense)
    def getPV(self,pokemon):
        if pokemon == "Salameche":
            self.__pv = 90
        if pokemon == "Carapuce":
            self.__pv = 110
        if pokemon == "Rattata":
            self.__pv = 120
        if pokemon == "Taupiqueur":
            self.__pv = 130
    def getpAttaque(self):
        print(self.pattaque)
    def setpAttaque(self, pa):
        self.pattaque = pa
    # def getDefense(self):
    #     return self.defense
    def setPV(self, pointsdevie):
        self.__pv = pointsdevie