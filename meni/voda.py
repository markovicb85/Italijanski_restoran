from meni.osnovna_stavka import OsnovnaStavka


class Voda(OsnovnaStavka):

    def __init__(self, naziv, cena, zapremina = 330):
        super().__init__(naziv, cena)
        self._zapremina = zapremina

    def __str__(self):
        return (f'Voda {self._naziv}: {self._cena} din, zapremina: {self._zapremina} ml')