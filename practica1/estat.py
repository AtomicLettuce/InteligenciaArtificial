from ia_2022 import entorn
from practica1 import joc
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio

"""
Posicio granota
percep[ClauPercepcio.POSICIO]['Miquel'][0]
o
self.info[0]

Posicio Paret
percep[ClauPercepcio.PARETs][0][0]

Posicio pizza
percep[ClauPercepio.OLOR][0]
"""
class Estat:

    def __init__(self, posicio:tuple, pes:int, pare=None):
        #posició son dos ints (coordX, coordY))
        self.__posicio=posicio
        #pare és un estat i sa acció que l'ha generat
        self.__pare=pare
        self.__pes=pes

    def eq(self, other) -> bool:
        return self.__posicio[0] ==other.__posicio[0] & self.__posicio[1]==other.__posicio[1]

    def es_meta(self,percep) -> bool:
        return (percep[ClauPercepcio.OLOR][0]==self.__posicio[0]) and (percep[ClauPercepcio.OLOR][1]==self.__posicio[1])

    def hash(self):
        return hash(tuple(self.__posicio))

    def __lt__(self, other):
        return False

    def __getitem__(self,key):
        return self.__posicio[key]

    def __setitem__(self, key, value):
        self.__posicio[key] = value

    def es_legal(self,percep) -> bool:

            for i in range(len(percep[ClauPercepcio.PARETS])):
                if ((self.__posicio[0] == percep[ClauPercepcio.PARETS][i][0]) 
                and (self.__posicio[1] == percep[ClauPercepcio.PARETS][i][1])):
                    #print("fals")
                    return False
           
            for i in range(2):
                if self.__posicio[i] >= percep[ClauPercepcio.MIDA_TAULELL][i]:
                    return False
                if self.__posicio[i] < 0:
                    return False
            return True
            


    def calcular_heuristica(self, percep)->int:
        pos_pizza=percep[ClauPercepcio.OLOR]
        sum=0
        sum=abs(pos_pizza[0]-self.__posicio[0])+abs(pos_pizza[1]-self.__posicio[1])
        return sum+self.__pes



        
    # Un pare és un Estat amb una acció
    @property
    def pare(self):
        return self.__pare

    @property
    def posicio(self):
        return self.__posicio

    @pare.setter
    def pare(self, value):
        self.__pare = value

    def genera_fills(self, percep):

        fills=[]
        
        # Fills ACCIÓ MOURE
        for i in Direccio:
            x,y = self.__posicio
            if i==Direccio.DRETA:
                x=x+1
            if i==Direccio.ESQUERRE:
                x=x-1
            if i==Direccio.BAIX:
                y=y+1
            if i==Direccio.DALT:
                y=y-1
            
            nou_fill=Estat((x,y),self.__pes+1,(self,(AccionsRana.MOURE,i)))
            
            if nou_fill.es_legal(percep,"", ""):
                fills.append(nou_fill)    

        # Fills ACCIÓ BOTAR
        for i in Direccio:
            x,y = self.__posicio
            if i==Direccio.DRETA:
                x=x+2
            if i==Direccio.ESQUERRE:
                x=x-2
            if i==Direccio.BAIX:
                y=y+2
            if i==Direccio.DALT:
                y=y-2
            
            nou_fill=Estat((x,y),self.__pes+6,(self,(AccionsRana.BOTAR,i)))
            
            if nou_fill.es_legal(percep,"",""):
                fills.append(nou_fill)  

        # Fill ACCIÓ ESPERAR
        #nou_fill=Estat((x,y),self.__pes+0.5,(self,(AccionsRana.ESPERAR)))
        fills.append(nou_fill)

        return fills

   