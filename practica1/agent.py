"""

ClauPercepcio:
    POSICIO = 0
    OLOR = 1
    PARETS = 2
"""
from ia_2022 import entorn
from practica1 import joc, agent_A_estrella
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio
from estat import Estat


class Rana(joc.Rana):
    
    def __init__(self, *args, **kwargs):
        super(Rana, self).__init__(*args, **kwargs)

    def pinta(self, display):
        pass

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:

        estat_inicial = Estat()
        estat_inicial.init(percep[ClauPercepcio.POSICIO],0, pare=None)

        estat_inicial.es_legal(percep)
        return AccionsRana.ESPERAR

