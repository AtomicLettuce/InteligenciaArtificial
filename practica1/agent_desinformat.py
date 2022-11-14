"""

ClauPercepcio:
    POSICIO = 0
    OLOR = 1
    PARETS = 2
"""
from ia_2022 import entorn
from practica1 import joc
from estat import Estat
from queue import PriorityQueue
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio
from practica1.agent import Estat


class RanaDesinformada(joc.Rana):   
     
    def __init__(self, *args, **kwargs):
        super(RanaDesinformada, self).__init__(*args, **kwargs)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def cerca(self, estat, percep):
        self.__oberts = []
        self.__tancats = set()

        self.__oberts.append(estat)
        actual = None
        while len(self.__oberts) > 0:
            actual = self.__oberts[0]
            self.__oberts = self.__oberts[1:]

            if actual in self.__tancats:
                continue
            
            estats_fills = actual.genera_fills(percep)

            if actual.es_meta(percep):
                break

            for estat_f in estats_fills:
                self.__oberts.append(estat_f)
            
            self.__tancats.add(actual)

        if actual is None:
            raise ValueError("Error impossible")

        if actual.es_meta(percep):
            accions = []
            iterador = actual

            while iterador.pare is not None:
                pare, accio = iterador.pare
                accions.append(accio)
                iterador = pare
            self.__accions = accions


    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat_inicial = Estat(percep[ClauPercepcio.POSICIO]['Miquel'],0, pare = None)
        if self.__accions is None:
            self.cerca( estat_inicial,percep)

            if self.__accions:
                acc = self.__accions.pop()
                if(acc == AccionsRana.ESPERAR):
                    return acc
                else:
                    return acc[0], acc[1]

            return AccionsRana.ESPERAR