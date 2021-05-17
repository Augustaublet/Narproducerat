class Event:
    def __init__(self, date, rekoring):
        self.__date = date
        self.__rekoring = rekoring
        self.__attending_producers = {}
        for producer in rekoring.get_joined_producers():
            self.__attending_producers[producer] = False

    def get_date(self):
        return self.__date
    
    def set_date(self, date):
        self.__date = date

    def get_rekoring(self):
        return self.__rekoring

    def get_attending_producers(self):
        '''
        Returns a list of producers confirmed to attend the current event.
        '''
        l = []
        for producer in self.__attending_producers:
            if self.__attending_producers[producer] == True:
                l.append(producer)
        return l
    
    def add_attending_producer(self, producer):
        '''
        Takes a producer and sets its value to True in the dictionary of attending producers.
        '''
        self.__attending_producers[producer] = True

    def remove_attending_producer(self, producer):
        '''
        Takes a producer and sets its value to False in the dictionary of attending producers.
        '''
        self.__attending_producers[producer] = False

    def get_id(self):
        return id(self)