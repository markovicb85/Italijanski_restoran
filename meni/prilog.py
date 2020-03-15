from meni.osnovna_stavka import OsnovnaStavka


class Prilog(OsnovnaStavka):

    def __init__(self, naziv, cena):
        super().__init__(naziv, cena)

    def __str__(self):
        return (f' {self._naziv}')