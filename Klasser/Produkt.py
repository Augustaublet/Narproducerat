class Produkt:
    def __init__(self, name, price, producer):
        self.__name = name
        self.__price = price
        self.__producer = producer
    
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_producer(self):
        return self.__producer

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price



