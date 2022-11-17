from ia_2022 import entorn
from practica1 import joc
from estat import Estat
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio
from random import randint, choice


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
    
    def __init__(self, pos_inicial:tuple, accions=None):
        self.__accions=accions
        self.__pos_inicial=pos_inicial
        self.__pos_final=pos_inicial
    
    def ha_arribat(self,percep)->bool:
        return self.__pos_final[0]==percep[ClauPercepcio.OLOR][0]and self.__pos_final[1]==percep[ClauPercepcio.OLOR]
    
    # Donada una acció sobre una rana mira si és legal (no se surt del mapa, no se fica dins una paret) i actualitza __pos_final
    def es_legal(self,accio, percep):
        if accio==AccionsRana.ESPERAR:
            return True
        if accio[0]==AccionsRana.MOURE:
            if accio[1]==Direccio.DRETA:
                if self.__pos_final[0]+1>percep[ClauPercepcio.MIDA_TAULELL][0] or (self.__pos_final[0]+1,self.__pos_final[1]) in ClauPercepcio.PARETS:
                    return False
                self.__pos_final=(self.__pos_final[0]+1,self.__pos_final[1])
            if accio[1]==Direccio.ESQUERRE:
                if self.__pos_final[0]-1<0 or (self.__pos_final[0]-1,self.__pos_final[1]) in ClauPercepcio.PARETS:
                    return False
                self.__pos_final=(self.__pos_final[0]-1,self.__pos_final[1])
            if accio[1]==Direccio.DALT:
                if self.__pos_final[1]-1<0 or (self.__pos_final[0],self.__pos_final[1]-1) in ClauPercepcio.PARETS:
                    return False
                self.__pos_final=(self.__pos_final[0],self.__pos_final[1]-1)
            if accio[1]==Direccio.BAIX:
                if self.__pos_final[1]+1>percep[ClauPercepcio.MIDA_TAULELL][0] or (self.__pos_final[0],self.__pos_final[1]+1) in ClauPercepcio.PARETS:
                    return False
                self.__pos_final=(self.__pos_final[0],self.__pos_final[1]+1)
                pass
        
        return True
    @property
    def accions(self):
        return self.__accions

    # indica quants de moviments vol generar per aquest individu
    def genera_moviments(self, qt:int, percep):
        self.__accions=[]


        for i in range(qt):
            a=self.acc_pos[randint(0,len(self.acc_pos))]
            if self.es_legal(a,percep):
                self.__accions.append(a)
    


    def calcula_fitness(self, percep):
        fitness=0
        # Distància Manhattan a sa pizza
        fitness= abs(percep[ClauPercepcio.OLOR][0]-self.__pos_final[0])+abs(percep[ClauPercepcio.OLOR][1]-self.__pos_final[1])

        # Penalitzam fer moviments inútils
        # 80% distància manhattan 20% quantitat de moviments
        fitness=80*fitness+20*len(self.__accions)


        return fitness

    def muta(self, percep):
        # sel·lecciona un moviment aleatori 
        idx = randint(0,len(self.__accions))

        # canvia aquest moviment per un altre moviment aleatori
        nova_acc=randint(0,len(self.acc_pos))
        self.__accions[idx]=nova_acc

    
    def offspring(self, other, qt:int):
        fills=[]

        for i in range(qt):
            pare_dominant=choice([True,False])
            # Seleccionar 'a' primers moviments de pare (self) + 'b' darrers moviments de mare (other)
            if pare_dominant:
                a=randint(1,len(self.__accions))
                b=randint(1,other.accions)
                
                fill = #Individu(ClauPercepcio.POSICIO,None)
                pass
            # Seleccionar 'a' primers moviments de pare (other) + 'b' darrers moviments de mare (self)
            else:
                pass

            pass
        # Seleccionar 'a' primers moviments de pare (self) + 'b' darrers moviments de mare (other)




        return fills