from Klasser.shopping_cart import ShoppingCart # type: ignore
class Consumer(ShoppingCart):
    def __init__(self, name, email):
        super().__init__()
        self.__name = name
        self.__email = email
        self.__order_history = []

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
        self.__order_history.append(current_order)

    def get_order_history(self):
        return self.__order_history

    def make_purchase(self):
        pass