from ia_2022 import entorn
from practica1 import joc
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio

"""
Posicio granota
percep[ClauPercepcio.POSICIO]['Miquel'][0]

Posicio Paret
percep[ClauPercepcio.PARETs][0][0]
"""
class Estat:

    def init(self, info:tuple, pes:int, pare=None):
        #info son dos ints (coordX, coordY))
        self.__info=info
        #pare és un estat i sa acció que l'ha generat
        self.__pare=pare
        self.__pes=pes

    def eq(self, other) -> bool:
        return self.info[0] ==other.info[0] & self.info[1]==other.info[1]

    def es_meta(self) -> bool:
        return ClauPercepcio.OLOR[0]==self.info[0] & ClauPercepcio.OLOR[1]==self.info[1]

    def hash(self):
        return hash(tuple(self.info))

    def __getitem__(self,key):
        return self.__info[key]

    def __setitem__(self, key, value):
        self.__info[key] = value

    @property
    def info(self):
        return self.info


    def genera_fill(self) -> list:
        estats_generats = []
        for accio in 4:
            nou_estat = copy.deepcpy(self)
            nou_estat.pare = (self, accio)

        return estats_generats


    def es_legal(self,percep) -> bool:
        print("es legal")

        for i in range(len(percep[ClauPercepcio.PARETS])):
            if ((percep[ClauPercepcio.POSICIO]['Miquel'][0] == percep[ClauPercepcio.PARETS][i][1]) 
            and (percep[ClauPercepcio.POSICIO]['Miquel'][0] == percep[ClauPercepcio.PARETS][i][1])):
                print("fals")
                return False
         
        
        for i in range(2):
            if percep[ClauPercepcio.POSICIO]['Miquel'][i] >= percep[ClauPercepcio.MIDA_TAULELL][i]:
                return False
            if percep[ClauPercepcio.POSICIO]['Miquel'][i] < 0:
                return False
        print("true")
        return True

    def calcular_heuristica(self)->int:
        pass

    # Un pare és un Estat amb una acció
    @property
    def pare(self):
        return self.__pare

    @pare.setter
    def pare(self, value):
        self.__pare = value

    def genera_fills(self):

        fills=[]
        
        # Fills ACCIÓ MOURE
        for i in Direccio:
            x,y = self.__info
            if i==Direccio.DRETA:
                x=x+1
            if i==Direccio.ESQUERRE:
                x=x-1
            if i==Direccio.BAIX:
                y=y+1
            if i==Direccio.DALT:
                y=y-1
            
            nou_fill=Estat((x,y),self.__pes+1,(self, (AccionsRana.MOURE, i)))
            
            if nou_fill.es_legal():
                fills.append(nou_fill)    

        # Fills ACCIÓ BOTAR
        for i in Direccio:
            x,y = self.__info
            if i==Direccio.DRETA:
                x=x+2
            if i==Direccio.ESQUERRE:
                x=x-2
            if i==Direccio.BAIX:
                y=y+2
            if i==Direccio.DALT:
                y=y-2
            
            nou_fill=Estat((x,y),self.__pes+6,(self, (AccionsRana.BOTAR, i)))
            
            if nou_fill.es_legal():
                fills.append(nou_fill)  

        # Fill ACCIÓ ESPERAR
        nou_fill=Estat((x,y),self.__pes+0.5,(self, (AccionsRana.ESPERAR)))
        fills.append(nou_fill)

