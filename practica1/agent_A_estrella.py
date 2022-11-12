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


class Rana(joc.Rana):
    
    def __init__(self, *args, **kwargs):
        super(Rana, self).__init__(*args, **kwargs)
        self.__oberts=None
        self.__tancats=None
        self.__accions=None

    def pinta(self, display):
        pass

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:

        estat_inicial=Estat(percep(ClauPercepcio.POSICIO),0, pare=None)

        if self.__accions is None:
            self.cerca(estat_inicial)
        
        if self.__accions:
            acc=self.__accions.pop()
        
        return acc
        
        return AccionsRana.ESPERAR
    
    def cerca(self, estat_inicial):
        self.__oberts = PriorityQueue()
        self.__tancats=set()
        self.oberts.put(estat_inicial.get_heuristica(), estat_inicial)

        actual = None

        while  not self.obers.empty():
            _, actual=self.oberts.get()
            if actual in self.tancats:
                continue
            if actual.es_meta()

