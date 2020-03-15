from meni.osnovna_stavka import OsnovnaStavka


class Pasta(OsnovnaStavka):

    def __init__(self, naziv, cena):
        super().__init__(naziv, cena)

    def __str__(self):
        return (f'Pizza {self._naziv}: {self._cena} din')