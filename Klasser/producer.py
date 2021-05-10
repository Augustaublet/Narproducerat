class Producer:

    def __init__(self, name, email, description, presentation):

        self.__name = name
        self.__email = email
        self.__description = description
        self.__presentation = presentation
        inventory = []

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
        inventory.append(product)

    def get_inventory(self):
        return inventory

    def remove_from_inventory(self, product):
        inventory.remove(product)
    






