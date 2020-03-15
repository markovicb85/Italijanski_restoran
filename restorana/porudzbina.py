from datetime import datetime

from meni import prilog
from meni.prilog import Prilog



class Porudzbina():

    def __init__(self, stavka, prilog = None, kolicina = 1, datum = datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        self._stavka = stavka
        self._prilog = prilog
        self._kolicina = kolicina
        self._datum = datum


    # @property
    # def hrana(self):
    #     return self._hrana
    #
    # @hrana.setter
    # def hrana(self, hrana):
    #     if isinstance(hrana, list):
    #         self._hrana = hrana
    #     else:
    #         return TypeError('Pogrsan tip')
    #
    # @property
    # def pice(self):
    #     return self._pice
    #
    # @hrana.setter
    # def pice(self, pice):
    #     if isinstance(pice, list):
    #         self._pice = pice
    #     else:
    #         return TypeError('Pogrsan tip')
    #
    # @property
    # def prilog(self):
    #     return self._prilog
    #
    # @hrana.setter
    # def prilog(self, prilog):
    #     if isinstance(prilog, Prilog):
    #         self._prilog = prilog
    #     else:
    #         return TypeError('Pogrsan tip')


    def stampanje_porudzbine(self):
        str = ''
        if self._kolicina > 1:
            str += f'{self._kolicina} x '

        if isinstance(self._stavka, list):
            for s in self._stavka:
                str += f'{s._naziv}, '
        else:
            str += self._stavka._naziv

        if self._prilog:
            if isinstance(self._prilog, list):
                for p in self._prilog:
                    str += f' + {p._naziv}'
            else:
                str += f' + {self._prilog._naziv}'

        return str.rstrip(', ')