class RekoRing:
    def __init__(self, name, region, place, time):
        self.__name = name
        self.__region = region
        self.__place = place
        self.__time = time
        self.__joined_producers = []

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_region(self):
        return self.__region
    
    def set_region(self, region):
        self.__region = region
    
    def get_place(self):
        return self.__place

    def set_place(self, place):
        self.__place = place
    
    def get_time(self):
        return self.__time
    
    def set_time(self, time):
        self.__time = time

    def get_joined_producers(self):
        '''
        Returns the list of joined producers.
        '''
        return self.__joined_producers
    
    def add_producer(self, producer):
        '''
        Takes a producer and adds it to the list of joined producers.
        '''
        self.__joined_producers.append(producer)
    
    def remove_producer(self, producer):
        '''
        Takes a producer and removes it from the list of joined producers.
        '''
        self.__joined_producers.remove(producer)

    def get_id(self):
        return id(self)

    