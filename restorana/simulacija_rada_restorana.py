import random

from datetime import datetime
from meni.voda import Voda
from meni.gazirani_sok import GaziraniSok
from meni.negazirani_sok import NegaziraniSok
from meni.pasta import Pasta
from meni.pizza import Pizza
from meni.prilog import Prilog
from restorana.porudzbina import Porudzbina
from restorana.porudzbina_exception import PorudzbinaException
from restorana.racun import Racun
from restorana.sto import Sto


def prikazi_poruceno(sto):
    print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    for i,p in enumerate(sto.porudzbina):
        print(f'{i}. {p.stampanje_porudzbine()}')
        i += 1


def main():

    #Pizze
    pizza_1 = Pizza('Capricciosa', random.randint(300, 601))
    pizza_2 = Pizza('Siciliana', random.randint(300, 601))
    pizza_3 = Pizza('Margarita', random.randint(300, 601))
    pizza_4 = Pizza('Quattro Stagioni', random.randint(300, 601))

    #Paste
    pasta_1 = Pasta('Italiana', random.randint(300, 601))
    pasta_2 = Pasta('Carbonara', random.randint(300, 601))
    pasta_3 = Pasta('Pasta Frutti Di Mare', random.randint(300, 601))
    pasta_4 = Pasta('Pasta Karbonara', random.randint(300, 601))
    pasta_5 = Pasta('Pasta Bolonjeze', random.randint(300, 601))

    #Pice
    pice_1 = Voda('Rosa', random.randint(150, 501))
    pice_2 = GaziraniSok('Coca-Cola', random.randint(150, 501))
    pice_3 = NegaziraniSok('Jabuka', random.randint(150, 501), '0.25')

    #Prilozi
    prilog_1 = Prilog('extra cheese', random.randint(300, 601))
    prilog_2 = Prilog('kecap', random.randint(300, 601))
    prilog_3 = Prilog('origano', random.randint(300, 601))
    prilog_4 = Prilog('pomfrit', random.randint(300, 601))
    prilog_5 = Prilog('urnebes', random.randint(300, 601))


    #Kreiranje porudzbine
    sto_1 = Sto(1, [
        Porudzbina(stavka = pizza_1,prilog = [prilog_2, prilog_3]),
        Porudzbina(stavka = pasta_1, prilog = prilog_1),
        Porudzbina(stavka = pice_2, kolicina = 2)], False)

    sto_2 = Sto(2, [
        Porudzbina(stavka = pizza_2),
        Porudzbina(stavka = pasta_2),
        Porudzbina(stavka = pice_3)], False)

    sto_3 = Sto(3, [
        Porudzbina(stavka=pizza_1, kolicina = 3, prilog = [prilog_2, prilog_2]),
        Porudzbina(stavka=pasta_2),
        Porudzbina(stavka = [pice_1, pice_2, pice_3])], False)

    sto_4 = None

    #Prikazi porudzbine
    print('\nSto br.1 porudzbina:')
    prikazi_poruceno(sto_1)


    print('\nSto br.2 porudzbina:')
    prikazi_poruceno(sto_2)

    print('\nSto br.3 porudzbina:')
    prikazi_poruceno(sto_3)

    #Naplata 1 i 3 porudzbine
    print('\nNaplata 1 i 3 stola: ')
    racun_1 = Racun(sto_1)
    racun_1.ukupno_za_placanje(sto_1)
    sto_1._placeno = True

    racun_3 = Racun(sto_3)
    racun_3.ukupno_za_placanje(sto_3)
    sto_3._placeno = True

    #Kreiranje nove porudzbine za sto br 2
    print('\nNova porudzbina za sto br.2:')
    try:
        sto_2.naruci()
    except PorudzbinaException as e:
        print(e)
        raise

if __name__ == '__main__':
    main()