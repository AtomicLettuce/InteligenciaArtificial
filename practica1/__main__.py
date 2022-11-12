import sys
#Posar es directori des NOSTRE REPOSITORI 
sys.path.append('C:\\Users\\xvive\\OneDrive - Universitat de les Illes Balears\\Escriptori\\UIBB3\\IA\\InteligenciaArtificial') #Cas Xavier
sys.path.append('C:\\*POSAR DIRECTORI LLUÍS*') #Cas Lluís

from practica1 import agent, joc


def main():
    rana = agent.Rana("Miquel")
    lab = joc.Laberint([rana], parets=True)
    lab.comencar()



if __name__ == "__main__":
    main()
