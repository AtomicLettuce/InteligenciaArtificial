import sys
#Posar es directori des NOSTRE REPOSITORI 
sys.path.append('C:\\Users\\xvive\\OneDrive - Universitat de les Illes Balears\\Escriptori\\UIBB3\\IA\\InteligenciaArtificial') #Cas Xavier
sys.path.append('C:\\Users\\lluis\\OneDrive\\Escritorio\\UIB\\3r\\IA\\INTELIGENCIAARTIFICIAL')#Cas Lluís

from practica1 import agent, joc,agent_A_estrella, agent_desinformat,agent_genetic,agent_minomax
from ia_2022 import entorn
from practica1 import joc
from estat import Estat
from queue import PriorityQueue
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio


def main():
    #SEL·LECCIONAR AGENT

    #rana = agent_desinformat.RanaDesinformada("Xavier")
    #rana = agent_A_estrella.Rana_A_Estrella("Xavier")
    #rana = agent_genetic.RanaGenetica("Xavier")
    #min = agent_minomax.agent_minomax("Xavier")
    #max = agent_minomax.agent_minomax("Lluis")
    lab = joc.Laberint([rana], parets=True)
    lab.comencar()




if __name__ == "__main__":
    main()
