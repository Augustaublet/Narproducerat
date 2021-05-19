from Klasser.shopping_cart import ShoppingCart # type: ignore

class Producer(ShoppingCart):

    def __init__(self, name, email, description, presentation):

        self.__name = name
        self.__email = email
        self.__description = description
        self.__presentation = presentation
        self.__inventory = []
        self.__user_type = "producer"

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

    def get_presentation(self):
        return self.__presentation

    def set_presentation(self, presentation):
        self.__presentation = presentation

    def add_to_inventory(self, product):
        '''
        Takes a product and adds it to the producers inventory list.
        '''
        self.__inventory.append(product)

    def get_inventory(self):
        return self.__inventory

    def remove_from_inventory(self, product):
        '''
        Takes a product and removes it from the producers inventory list.
        '''
        self.__inventory.remove(product)
    
    def get_id(self):
        return id(self)
    
    def get_user_type(self):
        return self.__user_type

    def get_last_orders(self,consumers):
        '''
        Returns the a dict with the consumer how ordered ass key and the 
        last order conectet to that consumer.
        '''
        current_order = {}
        for consumer in consumers:
            orders = consumer.get_order_history()
            if orders[0] == "Ingen order lagd":
                continue
            current_order[consumer]=orders[0]
        return current_order


