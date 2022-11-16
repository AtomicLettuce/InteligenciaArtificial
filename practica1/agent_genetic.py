from ia_2022 import entorn
from practica1 import joc
from estat import Estat
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio
from random import randint


class RanaGenetica(joc.Rana):

    def __init__(self, *args, **kwargs):
        super(RanaGenetica, self).__init__(*args, **kwargs)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None
    
    def pinta(self, display):
        pass

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
    
        return AccionsRana.ESPERAR

class Individu:
    # Totes les accions que se poden fer
    acc_pos=[AccionsRana.ESPERAR]
    for d in Direccio:
        ac=(AccionsRana.MOURE,d)
        acc_pos.append(ac)
        ac=(AccionsRana.BOTAR,d)
        acc_pos.append(ac)
    
    def __init__(self, pos_inicial:tuple):
        self.__accions=None
        self.__pos_inicial=pos_inicial
        self.__pos_final=pos_inicial
    
    def ha_arribat(self,percep)->bool:
        return self.__pos_final[0]==percep[ClauPercepcio.OLOR][0]and self.__pos_final[1]==percep[ClauPercepcio.OLOR]
    
    def es_legal(self,accio, percep):
        if accio==AccionsRana.ESPERAR:
            return True
        if accio[0]==AccionsRana.MOURE:
            if accio[1]==Direccio.DRETA:
                if self.__pos_final[0]+1>percep[ClauPercepcio.MIDA_TAULELL][0] or (self.__pos_final[0]+1,self.__pos_final[1]) in ClauPercepcio.PARETS:
                    return False
            if accio[1]==Direccio.ESQUERRE:
                pass
            if accio[1]==Direccio.DALT:
                pass
            if accio[1]==Direccio.BAIX:
                pass



        pass



    #indica quants de moviments vol generar per aquest individu
    def genera_moviments(self, qt:int, percep):
        self.__accions=[]


        for i in range(qt):
            a=self.acc_pos[randint(0,len(self.acc_pos))]
            if es_legal(a,percep):
                self.__accions.append(a)