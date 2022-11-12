from ia_2022 import entorn
from practica1 import joc
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio

class Estat:
    def init(self, info:int[], pes:int, pare=None):
        self.info=info
        self.pare=pare
        self.pes=pes

    def eq(self, other: Estat) -> bool:
        return self.info[0] ==other.info[0] & self.info[1]==other.info[1]

    def es_meta(self) -> bool:
        return ClauPercepcio.OLOR[0]==self.info[0] & ClauPercepcio.OLOR[1]==self.info[1]

    def hash(self):
        return hash(tuple(self.info))

    @property
    def info(self):
        return self.info


    def genera_fill(self) -> list:
        estats_generats = []
        for accio in 4:
            nou_estat = copy.deepcpy(self)
            nou_estat.pare = (self, accio)

        return estats_generats


    def es_legal(self) -> bool:
        for i in ClauPercepcio.PARETS:
            if percep(ClauPercepcio.POSICIO) == ClauPercepcio.PARETS[i]:
                return False
        for i in 2
            if ClauPercepcio.POSICIO[i] >= ClauPercepcio.MIDA_TAULELL[i]:
                return False
            if ClauPercepcio.POSICIO[i] < 0:
                return False
        return True

    def get_heuristica(self)->int:
        pass

    @property
    def pare(self):
        return self.pare

    @pare.setter
    def pare(self, value):
        self.__pare = value