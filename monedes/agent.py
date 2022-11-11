""" Mòdul que conté l'agent per jugar al joc de les monedes.

Percepcions:
    ClauPercepcio.MONEDES
Solució:
    " XXXC"
"""

from queue import PriorityQueue
from tokenize import String
from entorn import AccionsMoneda, ClauPercepcio
from ia_2022 import agent, entorn
import copy

SOLUCIO = " XXXC"
class Estat:

    def __init__(self, info: dict=None, pare=None) -> None:
        if info is None:
            info={}
        self.__info=info
        self.__pare=pare

    def es_meta(self) ->bool:
        return self.__info==" XXXC"
    
    def genera_fills(self)->list:
        estats_generats=[]

        # Girar moneda
        for i in range(5):
            nou_estat=copy.deepcopy(self)
            if(self.__info[i]!=" "):
                if(self.__info[i]=="X"):
                    nou_estat.__info[i]="C"
                else:
                    nou_estat.__info[i]="X"
            nou_estat.__pare=(AccionsMoneda.GIRAR,i)
            estats_generats.append(nou_estat)

        # Botar moneda
        for i in range(5):
            if(self.__info[i]==" "):
                if i+2<5:
                    nou_estat=copy.deepcopy(self)
                    nou_estat.__info[i+2]=" "
                    if(self.__info[i+2]=="X"):
                        nou_estat.__info[i]="C"
                        nou_estat.__pare=(AccionsMoneda.BOTAR,i+2)
                    else:
                        nou_estat.__info[i]="X"
                        nou_estat.__pare=(AccionsMoneda.BOTAR,i+2)
                    estats_generats.append(nou_estat)
                if i-2>-1:
                    nou_estat=copy.deepcopy(self)
                    nou_estat.__info[i-2]=" "
                    if(self.__info[i-2]=="X"):
                        nou_estat.__info[i]="C"
                        nou_estat.__pare=(AccionsMoneda.BOTAR,i-2)
                    else:
                        nou_estat.__info[i]="X"
                        nou_estat.__pare=(self,AccionsMoneda.BOTAR,i-2)
                    estats_generats.append(nou_estat)
        
        #Desplaçar moneda
        for i in range(5):
            if(self.__info[i]==" "):
                if i+1<5:
                    nou_estat=copy.deepcopy(self)
                    nou_estat.__info[i+1]=" "
                    nou_estat.__info[i]=self.__info[i]
                    nou_estat.__pare=(self,AccionsMoneda.DESPLACAR,i)
                    estats_generats.append(nou_estat)
                if i-1>-1:
                    nou_estat=copy.deepcopy(self)
                    nou_estat.__info[i-1]=" "
                    nou_estat.__info[i]=self.__info[i]
                    nou_estat.__pare=(self,AccionsMoneda.DESPLACAR,i)
                    estats_generats.append(nou_estat)
        return estats_generats
                
    def get_heurisitica(self):
        heuristica=0
        heuristica+= self.__info.find(" ")

        if(self.__info[1]!="X"):
            heuristica+=1
        if(self.__info[2]!="X"):
            heuristica+=1
        if(self.__info[3]!="X"):
            heuristica+=1
        if(self.__info[4]!="C"):
            heuristica+=1
            
        return heuristica


class AgentMoneda(agent.Agent):
    def __init__(self):
        super().__init__(long_memoria=0)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def pinta(self, display):
        print(self._posicio_pintar)

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:

        estat= Estat(percep[ClauPercepcio.MONEDES],pare=None)

        if self.__accions is None:
            self._cerca(estat)
        if len(self.__accions)>0:
            return AccionsMoneda.DESPLACAR ,self.__accions.pop()
        else:
            return AccionsMoneda.RES

    def _cerca(self, estat: Estat):
        _, self.__oberts=PriorityQueue()
        self.__tancats=set()

        self.__oberts.put((estat.get_heurisitica,estat))
        actual=None
        while not self.__oberts.empty():
            actual=self.__oberts.get()

            if actual in self.__tancats:
                continue
            if actual.es_meta():
                break
            
            fills=actual.genera_fills()
            for fill in fills:
                self.__oberts.put((fill.get_heuristica(),fill))

            self.__tancats.add(actual)

        if actual.es_meta():
            accions = []
            iterador = actual
            while iterador.pare is not None:
                pare,accio= iterador.pare
                accions.append(accio)
                iterador=pare
            self.__accions=accions


