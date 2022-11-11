import sys
sys.path.append('C:\\Users\\xvive\\OneDrive - Universitat de les Illes Balears\\Escriptori\\UIBB3\\IA\\ia_2022')

from quiques import agent_amplada, joc, agent_profunditat


def main():
    barca = agent_amplada.BarcaAmplada()
    illes = joc.Illes([barca])
    illes.comencar()


if __name__ == "__main__":
    main()
