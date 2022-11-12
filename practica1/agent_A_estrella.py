"""

ClauPercepcio:
    POSICIO = 0
    OLOR = 1
    PARETS = 2
"""
from ia_2022 import entorn
from practica1 import joc
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio

class Estat:
    def __init__(self, info:int[], pes:int, pare=None):
        self.__info=info
        self.__pare=pare
        self.__pes=pes
    
    def __eq__(self, other: Estat) -> bool:
        return self.__info[0] ==other.info[0] & self.__info[1]==other.info[1]

    def es_meta(self) -> bool:
        return ClauPercepcio.OLOR[0]==self.__info[0] & ClauPercepcio.OLOR[1]==self.__info[1]
    