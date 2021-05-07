class Produkt:
    def __init__(self, namn, pris, ägare):
        self.__namn = namn
        self.__pris = pris
        self.__ägare = ägare
    
    def get_namn(self):
        return self.__namn

    def get_pris(self):
        return self.__pris

    def get_ägare(self):
        return self.__ägare

    def set_namn(self, namn):
        self.__namn = namn

    def set_pris(self, pris):
        self.__pris = pris



