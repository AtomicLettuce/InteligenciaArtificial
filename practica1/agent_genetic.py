from ia_2022 import entorn
from practica1 import joc
from estat import Estat
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio


class RanaGenetica(joc.Rana):
     
    def __init__(self, *args, **kwargs):
        super(RanaGenetica, self).__init__(*args, **kwargs)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None
    
    def pinta(self, display):
        pass

    def cerca(self, estat, percep):
        self.__oberts = []
        
    