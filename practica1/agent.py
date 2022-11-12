"""

ClauPercepcio:
    POSICIO = 0
    OLOR = 1
    PARETS = 2
"""
from ia_2022 import entorn
from practica1 import joc
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio


class Rana(joc.Rana):
    
    def __init__(self, *args, **kwargs):
        super(Rana, self).__init__(*args, **kwargs)

    def pinta(self, display):
        pass

    def actua(
            self, percep: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        return AccionsRana.ESPERAR

class Estat:
    def __init__(self, info:str, pes:int, pare=None):
        self.__info = info
        self.__pare = pare
        self._pes = pes

    def __hash__(self):
        return hash(tuple(self.__info))

    @property
    def info(self):
        return self.__info


    def genera_fill(self) -> list:
        estats_generats = []
        for accio in 4:
            nou_estat = copy.deepcpy(self)
            nou_estat.pare = (self, accio)
        
        return estats_generats

        
    @property
    def pare(self):
        return self.__pare

    @pare.setter
    def pare(self, value):
        self.__pare = value