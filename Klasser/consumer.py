from shopping_cart import *
class Consumer(ShoppingCart):
    def __init__(self, name, email):
        super().__init__()
        self.__name = name
        self.__email = email

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_shopping_cart(self):
        return self.__shopping_cart

