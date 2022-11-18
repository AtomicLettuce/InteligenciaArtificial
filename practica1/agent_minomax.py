from ia_2022 import entorn
from practica1 import joc
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio

class agent_minomax(joc.Rana):   

    def __init__(self, *args, **kwargs):
        super(agent_minomax,self).__init__(*args, **kwargs)
        self.__accions = None
        self.__estatActual = None
        
    def pinta(self, display):
        pass

    def minimax(self,Estat,torn_de_max,percep):
        profunditat = 5
        if torn_de_max == profunditat:
            return self.evaluar(percep)
        print(max)
        print(max.__name__)
        #agafar es fill que tengui sa maxima o sa minima
        if torn_de_max % 2 == 0:
            puntuacio_fills = [self.minimax(estat_fill,torn_de_max+1) for estat_fill in Estat.genera_fills_minimax(percep,max.__name__,min.__name__)]
            return max(puntuacio_fills)
        else:
            puntuacio_fills = [self.minimax(estat_fill,torn_de_max+1) for estat_fill in Estat.genera_fills_minimax(percep,min.__name__,max.__name__)]
            return min(puntuacio_fills)
        

    def evaluar(self,percep):
        
        return Estat.calcular_distanciaManhatan(min.__name__,percep)-Estat.calcular_distanciaManhatan(max.__name__,percep)

    
    def cerca(self, estat, percep):
        self.minimax(estat,0,percep)

    #fer que no comenci cada vegada per s'estat inicial
    #nomes hi ha una accio cada vegada
    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        print(percep[ClauPercepcio.POSICIO])
        estat_inicial = Estat(percep[ClauPercepcio.POSICIO],None)
        
        self.cerca( estat_inicial,percep)

        return AccionsRana.ESPERAR



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

    def __init__(self, posicio:tuple,  pare=None):
        #posició es una tupla amb els agents i les seves posicions
        self.__posicio=posicio
        #pare és un estat i sa acció que l'ha generat
        self.__pare=pare

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

    def es_legal(self,percep,max,min) -> bool:
            for i in range(len(percep[ClauPercepcio.PARETS])):
                if ((self.__posicio[max][0] == percep[ClauPercepcio.PARETS][i][0]) 
                and (self.__posicio[max][1] == percep[ClauPercepcio.PARETS][i][1])):
                    #print("fals")
                    return False
           
            for i in range(2):
                if self.__posicio[max][i] >= percep[ClauPercepcio.MIDA_TAULELL][i]:
                    return False
                if self.__posicio[max][i] < 0:
                    return False


            if (self.__posicio[max][0] == self.__posicio[min][0]
            and self.__posicio[max][1] == self.__posicio[min][1]):
                return False            
            return True 

    def calcular_heuristica(self, percep)->int:
        pos_pizza=percep[ClauPercepcio.OLOR]
        sum=0
        sum=abs(pos_pizza[0]-self.__posicio[0])+abs(pos_pizza[1]-self.__posicio[1])
        return sum+self.__pes

    def calcular_distanciaManhatan(self, max, percep )->int:
        pos_pizza=percep[ClauPercepcio.OLOR]
        sum=0
        sum=abs(pos_pizza[0]-self.__posicio[max][0])+abs(pos_pizza[1]-self.__posicio[max][1])
        return sum

        
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



    def genera_fills_minimax(self, percep, max,min):

        fills=[]
        
        # Fills ACCIÓ MOURE
        for i in Direccio:
            print(max)
            x,y = self.__posicio[max]
            if i==Direccio.DRETA:
                x=x+1
            if i==Direccio.ESQUERRE:
                x=x-1
            if i==Direccio.BAIX:
                y=y+1
            if i==Direccio.DALT:
                y=y-1
            
            nou_fill=Estat((x,y),(self,(AccionsRana.MOURE,i)))
            
            if nou_fill.es_legal(percep,max,min):
                fills.append(nou_fill)    

        # Fills ACCIÓ BOTAR
        for i in Direccio:
            x,y = self.__posicio[max]
            if i==Direccio.DRETA:
                x=x+2
            if i==Direccio.ESQUERRE:
                x=x-2
            if i==Direccio.BAIX:
                y=y+2
            if i==Direccio.DALT:
                y=y-2
            
            nou_fill=Estat((x,y),(self,(AccionsRana.BOTAR,i)))
            
            if nou_fill.es_legal(percep,max,min):
                fills.append(nou_fill)  

        # Fill ACCIÓ ESPERAR
        #nou_fill=Estat((x,y),self.__pes+0.5,(self,(AccionsRana.ESPERAR)))
        fills.append(nou_fill)

        return fills





