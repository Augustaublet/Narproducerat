class ShoppingCart:

    def __init__(self):
        self.__cart_list = []
    
    def get_cart_list(self):
        return self.__cart_list

    def add_to_cart(self, product):
        self.__cart_list.append(product)

    def remove_from_cart(self, product):
        self.__cart_list.remove(product)

        