from datetime import datetime


class Racun():

    def __init__(self, sto, datum = datetime.now().strftime("%d/%m/%Y %H:%M:%S")):
        self.sto = sto
        self.datum = datum


    def ukupno_za_placanje(self, sto):
        sum = 0
        for p in sto.porudzbina:
            if isinstance(p._stavka, list):
                for s in p._stavka:
                    sum += s._cena
            else:
                sum += p._stavka._cena
                if p._kolicina > 1:
                    sum = sum * p._kolicina

            if isinstance(p._prilog, list):
                for p in p._prilog:
                    sum += p._cena
            elif p._prilog:
                sum += p._prilog._cena

        print(f'Racun: datum {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}, sto broj {sto._id}, naplata {sum} rsd')