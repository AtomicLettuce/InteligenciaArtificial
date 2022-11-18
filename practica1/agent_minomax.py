from ia_2022 import entorn
from practica1 import joc
from practica1.estat import Estat
from queue import PriorityQueue
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio

class agent_minomax(min = joc.Rana, max = joc.Rana):   
    profunditat = 5
    def __init__(self, *args, **kwargs):
        super(agent_minomax, self).__init__(*args, **kwargs)
        self.__accions = None
    
    def minimax(Estat,torn_de_max,percep):
        global profunditat
        if torn_de_max == profunditat:
            return evaluar(percep)
        
        #agafar es fill que tengui sa maxima o sa minima
        if torn_de_max % 2 == 0:
            puntuacio_fills = [minimax(estat_fill,torn_de_max+1) for estat_fill in Estat.genera_fills(max.__name__,min.__name__)]
            return max(puntuacio_fills)
        else:
            puntuacio_fills = [minimax(estat_fill,torn_de_max+1) for estat_fill in Estat.genera_fills(min.__name__,max.__name__)]
            return min(puntuacio_fills)
        

    def evaluar(percep):
        
        return Estat.calcular_distanciaManhatan(min.__name__,percep)-Estat.calcular_distanciaManhatan(max.__name__,percep)

    
    def cerca(self, estat, percep):
        minimax(estat,0,percep)
        
        


