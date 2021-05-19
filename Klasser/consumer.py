from Klasser.shopping_cart import ShoppingCart # type: ignore
import time
# from testobjekt import produkter, rekoringar, användare, producenter


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
        self.__order_history.insert(0,[current_order])

    def get_order_history(self):
        if self.__order_history:
            return self.__order_history
        else:
            return ["Ingen order lagd"]
    def make_purchase(self):
        new_dict = {}
        time_now = time.ctime()
        producers = self.get_producers()
        cart = self.get_cart_list()
        producer_dict = {}
        for producer in producers:
            product_cart = {}
            for product in cart:
                if product.get_producer() == producer:
                    product_cart[product] = cart[product]
            producer_dict[producer] = product_cart
        new_dict[time_now] = producer_dict
        

        # for x in new_dict:
        #     print(x)
        #     for y in new_dict[x]:
        #         print(y.get_name())
        #         for j in new_dict[x][y]:
        #             print(j.get_name(), new_dict[x][y][j])
                   
        self.add_to_history(new_dict)
        self.empty_cart()

    def get_user_type(self):
        return self.__user_type

