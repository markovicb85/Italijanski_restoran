


class Restoran():

    #Singleton
    _instance = None
    _lista_stolova = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Restoran, cls).__new__(cls)
        return cls._instance