import sys
sys.path.append('C:\\Users\\xvive\\OneDrive - Universitat de les Illes Balears\\Escriptori\\UIBB3\\IA\\ia_2022')

from aspirador import agent, joc


def main():
    aspirador = agent.AspiradorReflex()
    hab = joc.Casa([aspirador])
    hab.comencar()


if __name__ == "__main__":
    main()
