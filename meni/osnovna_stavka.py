
class OsnovnaStavka():

    def __init__(self, naziv, cena):
        self._naziv = naziv
        self._cena = cena


    def __str__(self):
        return (f'{self._naziv}: {self._cena} din')