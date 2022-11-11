import sys
sys.path.append('C:\\Users\\xvive\\OneDrive - Universitat de les Illes Balears\\Escriptori\\UIBB3\\IA\\ia_2022')
from monedes import agent, joc


def main():
    ag_mon = agent.AgentMoneda()
    joc_mon = joc.Moneda([ag_mon])
    joc_mon.comencar()


if __name__ == "__main__":
    main()
