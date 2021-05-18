from Klasser.shopping_cart import ShoppingCart # type: ignore
import time
class Consumer(ShoppingCart):
    def __init__(self, name, email):
        super().__init__()
        self.__name = name
        self.__email = email
        self.__order_history = []
        self.__user_type = "consumer"

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_id(self):
        return id(self)

    def get_current_order(self):
        order = self.get_cart_list()
        return order
    
    def add_to_history(self, current_order):
        #Jag har vänt på lista för att få senaste köpet först /aa
        self.__order_history.insert(0,[current_order,time.ctime()])

    def get_order_history(self):
        if self.__order_history:
            return self.__order_history
        else:
            return ["Ingen order lagd"]
    def make_purchase(self):
        self.add_to_history(self.get_cart_list())
        self.empty_cart()

    def get_user_type(self):
        return self.__user_type