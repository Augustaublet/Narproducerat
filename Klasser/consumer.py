class Consumer:

    def __init__(self, name, email, consumer_ID, shopping_cart):
        self.__name = name
        self.__email = email
        self.__consumer_ID = consumer_ID
        self.__shopping_cart = shopping_cart

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
    
    def get_consumerID(self):
        return self.__consumer_ID

    def get_shopping_cart(self):
        return self.__shopping_cart

