class Product:
    def __init__(self, name, price, producer, description="ingen beskrivng finns"):
        self.__name = name
        self.__price = price
        self.__producer = producer
        self.__description = description
        self.__quantity = None
    
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
        self.__quantity = quantity

    def __str__(self):
        return f"{self.__name}, {self.__price}, {self.__producer.get_name()}"
    
    def set_description(self, description):
        self.__description = description
    
    def get_description(self):
        return self.__description

