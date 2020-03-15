from restorana.porudzbina import Porudzbina
from restorana.porudzbina_exception import PorudzbinaException


class Sto():

    def __init__(self, id, porudzbina = None, placeno = True):
        self._id = id
        self.porudzbina = porudzbina
        self._placeno = placeno


    @property
    def porudzbina(self):
        return self._porudzbina

    @porudzbina.setter
    def porudzbina(self, value):
        if isinstance(value, list):
            self._porudzbina = value
        else:
            return ValueError('Pogresan tip')

    def naruci(self):
        if self._placeno:
           pass
        else:
            raise PorudzbinaException('Prethodni racun nije placen. Nije moguce kreirati novu porudzbinu', self.porudzbina)