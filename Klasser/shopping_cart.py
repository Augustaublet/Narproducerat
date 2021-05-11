class ShoppingCart:

    def __init__(self):
        self.__cart_list = {}

    def get_cart_list(self):
        return self.__cart_list

    def print_cart_products(self):
        '''
        Returns a dictionary of the products(key) and their prices(value) currently in the cart.
        '''
        cart = {}
        for product in self.__cart_list:
            cart[product.get_name()] = self.__cart_list[product]
        return cart

    def buy_product(self, product, amount):
        '''
        Takes a product(key) and how many you want to buy(value), and adds them to the cart dictionary.
        If the product is already in the cart, it updates the amount to the input added.
        '''
        self.__cart_list[product] = amount
     
    def remove_from_cart(self, product):
        '''
        Removes the product from the cart completely.
        '''
        self.__cart_list.remove(product)

    def get_consumer(self):
        return self.__consumer
