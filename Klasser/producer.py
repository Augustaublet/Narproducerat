class Producer:

    def __init__(self, name, description, presentation):

        self.__name = name
        self.__description = description
        self.__presentation = presentation

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

    def get_presentation(self):
        return self.__presentation

    def set_presentation(self, presentation):
        self.__presentation = presentation






