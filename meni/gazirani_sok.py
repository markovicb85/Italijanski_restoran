from meni.osnovna_stavka import OsnovnaStavka


class GaziraniSok(OsnovnaStavka):

    def __init__(self, naziv, cena, zapremina = 330):
        super().__init__(naziv, cena)
        self._zapremina = zapremina


    def __str__(self):
        return (f'Gazirani sok {self._naziv}: {self._cena} din, zapremina: {self._zapremina} ml')
