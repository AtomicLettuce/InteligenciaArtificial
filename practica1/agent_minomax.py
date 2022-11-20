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

    def minimax(self,Estat,torn_de_max,):
        profunditat = 4
        if torn_de_max == profunditat:
            return self.evaluar(Estat),Estat

        #agafar es fill que tengui sa maxima o sa minima
        if torn_de_max % 2 == 0:

            estats_fill = Estat.genera_fills_minimax()
            punmax = -999,None
            for i in range(len(estats_fill)):
                puntuacio = self.minimax(estats_fill[i],torn_de_max+1) 
                if puntuacio[0] >= punmax[0]:
                    punmax = puntuacio

            return punmax
        else:
            estats_fill = Estat.genera_fills_minimax()
            punmin = -999,None
            for i in range(len(estats_fill)):
                puntuacio = self.minimax(estats_fill[i],torn_de_max+1) 
                if puntuacio[0] >= punmin[0]:
                    
                    punmin= puntuacio
            return punmin
        
    
    def evaluar(self,estat):
        
        return Estat.calcular_distanciaManhatan(estat)

    def pinta(self,display):
        pass
    
    def cerca(self, estat):
        _,actual = self.minimax(estat,0)
        _, accio = actual.pare
        return accio

    #fer que no comenci cada vegada per s'estat inicial
    #nomes hi ha una accio cada vegada
    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        noms = list(percep[ClauPercepcio.POSICIO].keys())
        noms.remove(self.nom)
        estat_inicial = Estat(percep.to_dict(),percep[ClauPercepcio.POSICIO][self.nom],None,nomMax = self.nom,nomMin = noms[0])


        accio =  self.cerca(estat_inicial)
        #input()
        return accio


       



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

    def __init__(self,percep,pos, pare,nomMax,nomMin):
        #posició es una tupla amb els agents i les seves posicions
        self.percep = percep
        self.nomMax = nomMax
        self.nomMin = nomMin
        self.__posicio = pos
        #pare és un estat i sa acció que l'ha generat
        self.__pare=pare

    def es_meta(self,percep) -> bool:
        return (percep[ClauPercepcio.OLOR][0]==self.posicio[0]) and (percep[ClauPercepcio.OLOR][1]==self.posicio[1])

    def hash(self):
        return hash(tuple(self.posicio))

    def __lt__(self, other):
        return False

    @property
    def posicio(self):
        return self.__posicio

    def __getitem__(self,key):
        return self.posicio[key]

    def __setitem__(self, key, value):
        self.posicio[key] = value

    def es_legal(self,x,y) -> bool:
        
        for i in range(len(self.percep[ClauPercepcio.PARETS])):
                if ((x == self.percep[ClauPercepcio.PARETS][i][0]) 
                and (y == self.percep[ClauPercepcio.PARETS][i][1])):
                    #print("fals")
                    return False
           
        
        if x >= self.percep[ClauPercepcio.MIDA_TAULELL][0]:
            return False
        if x < 0:
            return False
        if y >= self.percep[ClauPercepcio.MIDA_TAULELL][1]:
            return False
        if y < 0:
            return False

        if(x == self.percep[ClauPercepcio.POSICIO][self.nomMin][0] and 
        y == self.percep[ClauPercepcio.POSICIO][self.nomMin][1]):
            return False  
        return True 




    def calcular_distanciaManhatan(self)->int:
        pos_pizza=self.percep[ClauPercepcio.OLOR]
        sum=0
        sum=abs(pos_pizza[0]-self.posicio[0])+abs(pos_pizza[1]-self.posicio[1])
        res=0
        res=abs(pos_pizza[0]-self.percep[ClauPercepcio.POSICIO][self.nomMin][0])+abs(pos_pizza[1]-self.percep[ClauPercepcio.POSICIO][self.nomMin][1])
        return res-sum

        
    # Un pare és un Estat amb una acció
    @property
    def pare(self):
        return self.__pare



    @pare.setter
    def pare(self, value):
        self.__pare = value



    def genera_fills_minimax(self):

        fills=[]
        # Fills ACCIÓ MOURE
        for i in Direccio:
            x,y= self.posicio
            if i==Direccio.DRETA:
                x=x+1
            if i==Direccio.ESQUERRE:
                x=x-1
            if i==Direccio.BAIX:
                y=y+1
            if i==Direccio.DALT:
                y=y-1
            

            nou_fill=Estat(self.percep, (x,y), (self,(AccionsRana.MOURE,i)),self.nomMax,self.nomMin)
            
            if nou_fill.es_legal(x,y):
                fills.append(nou_fill)    

        # Fills ACCIÓ BOTAR
        for i in Direccio:
            x,y = self.posicio
            if i==Direccio.DRETA:
                x=x+2
            if i==Direccio.ESQUERRE:
                x=x-2
            if i==Direccio.BAIX:
                y=y+2
            if i==Direccio.DALT:
                y=y-2
            

            nou_fill=Estat(self.percep,(x,y),(self,(AccionsRana.MOURE,i)),self.nomMax,self.nomMin)
          
            if nou_fill.es_legal(x,y):
                fills.append(nou_fill)  

        # Fill ACCIÓ ESPERAR
        nou_fill=Estat(self.percep,self.posicio,(self,(AccionsRana.ESPERAR)),self.nomMax,self.nomMin)
        fills.append(nou_fill)

        return fills





