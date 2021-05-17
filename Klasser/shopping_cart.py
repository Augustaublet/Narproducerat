class ShoppingCart:

    def __init__(self):
        self.__cart_list = {}

    def get_cart_list(self):
        return self.__cart_list

    def print_cart_products(self):
        '''
        Returns a dictionary of the products(key) and their total price(value) currently in the cart.
        '''
        cart = {}
        for product in self.__cart_list:
            cart[product.get_name()] = product.get_price()*self.__cart_list[product]
        return cart

    def add_x_products(self, product, amount):
        '''
        Takes a product(key) and how many you want to buy(value), and adds them to the cart dictionary.
        If the product is already in the cart, it updates the amount to the input added.
        If there is no stock or the stock would be lower than 0, it returns nothing.
        '''
        if product.get_quantity == None:
            print("Den här produkten har inget saldo.")
            return
        if product.get_quantity() - int(amount) > 0:
            product.set_quantity(product.get_quantity() - int(amount))
            self.__cart_list[product] = int(amount)
        else:
            print("Produkten är slutsåld.")

    def add_one_product(self, product):
        '''
        Takes a product and adds one piece to the cart.
        If the amount left in the producers inventory is 0, or is None, it prints a message.
        '''
        if product.get_quantity() == None:
            print("Den här produkten har inget saldo.")
            return
        if product.get_quantity() - int(1) > 0:
            if product not in self.__cart_list:
                product.set_quantity(product.get_quantity() - int(1))
                self.__cart_list[product] = int(1)
            else:    
                product.set_quantity(product.get_quantity() - int(1))
                self.__cart_list[product] += int(1)
        else:
            print("Produkten är slutsåld.")

    def subract_one_product(self, product):
        '''
        Takes a product and subtracts one piece from the cart.
        '''
        self.__cart_list[product] -= int(1)
        product.set_quantity(product.get_quantity() + int(1))

    def remove_from_cart(self, product):
        '''
        Removes the product from the cart completely.
        Restores the products amount in the cart to the producers inventory.
        '''
        product.set_quantity(product.get_quantity + self.__cart_list[product])
        self.__cart_list.remove(product)

    def get_consumer(self):
        return self.__consumer

    def get_producers(self):
        '''
        Returns a list of the producers who own the wares in the cart.
        '''
        producers = []
        for product in self.__cart_list:
            if product.get_producer() not in producers:
                producers.append(product.get_producer())
        return producers

    # def sum_per_producer(self):
    #     '''
    #     Returns a dictionary with the producers(key) and the sum of the cost of their products in the cart(value).
    #     '''
    #     dict = {}
    #     for producer in self.get_producers():
            
    def get_id(self):
        return id(self)

