class Product:
    def __init__(self, name, price, producer, description="Ingen beskrivning finns", for_sale=True):
        self.__name = name
        self.__price = int(price)
        self.__producer = producer
        self.__description = description
        self.__quantity = None
        self.__for_sale = for_sale

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

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = int(quantity)

    def __str__(self):
        return f"Namn: {self.__name}, Pris: {self.__price}, Kvantitet kvar: {self.__quantity}, Producent: {self.__producer.get_name()}"
    
    def set_description(self, description):
        self.__description = description
    
    def get_description(self):
        return self.__description

    #tar Boolean för om produkten är tillgänglig
    def set_is_for_sale(self, state):
        self.__for_sale = state

    def get_is_for_sale(self):
        return self.__for_sale

    def get_id(self):
        return id(self)
