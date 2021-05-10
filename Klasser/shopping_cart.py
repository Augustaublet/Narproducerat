class ShoppingCart:

    def __init__(self):
        self.__cart_list = {}

    def get_cart_list(self):
        return self.__cart_list

    def print_cart_products(self):
        cart = {}
        for product in self.__cart_list:
            cart[product.get_name()] = self.__cart_list[product]
            #print(f"{product.get_name()}, {self.__cart_list[product]}st.")
        return cart

    def buy_product(self, product, amount):
        self.__cart_list[product] = amount
     
    def remove_from_cart(self, product):
        self.__cart_list.remove(product)

    def get_consumer(self):
        return self.__consumer
