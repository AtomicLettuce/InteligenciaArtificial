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
import time


class Rana(joc.Rana):
    
    def __init__(self, *args, **kwargs):
        super(Rana, self).__init__(*args, **kwargs)
        self.__oberts=None
        self.__tancats=None
        self.__accions=None

    def pinta(self, display):
        pass

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat_inicial=Estat(percep[ClauPercepcio.POSICIO]['Xavier'],0,None)
        

        if self.__accions is None:
            self.cerca(estat_inicial, percep)

        
        if self.__accions:
            if self.esta_botant():
                return AccionsRana.ESPERAR
            acc=self.__accions.pop()
            if(acc==AccionsRana.ESPERAR):
                return acc
            else:
                return acc[0], acc[1]
        return AccionsRana.ESPERAR
        
        
    
    def cerca(self, estat_inicial, percep):
        self.__oberts = PriorityQueue()
        self.__tancats=set()
        self.__oberts.put((estat_inicial.calcular_heuristica(percep), estat_inicial))

        actual = None

        while  not self.__oberts.empty():
            _, actual=self.__oberts.get()

            if actual in self.__tancats:
                continue

            if actual.es_meta(percep):                
                break

            estats_fills=actual.genera_fills(percep)
            
            for fill in estats_fills:
                self.__oberts.put((fill.calcular_heuristica(percep),fill))
            
            self.__tancats.add(actual)

        if actual.es_meta(percep):
            accions=[]
            iterador=actual

            while iterador.pare is not None:
                pare, accio=iterador.pare

                accions.append(accio)
                iterador=pare
            
            self.__accions=accions


