from ia_2022 import entorn
from practica1 import joc
from estat import Estat
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio
from queue import PriorityQueue
from random import randint, choice


class RanaGenetica(joc.Rana):

    def __init__(self, *args, **kwargs):
        super(RanaGenetica, self).__init__(*args, **kwargs)
        self.__accions=None
    
    def pinta(self, display):
        pass

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        if self.esta_botant():
            return AccionsRana.ESPERAR
        if self.__accions is None:
            self.genera_individus(percep)

        if self.__accions:
            print(self.__accions)
            acc=self.__accions.pop()
            return acc
        # Perquè no se peti quan acaba
        return AccionsRana.ESPERAR

    def genera_individus(self, percep):
        solucio =None
        self.__accions=[]

        coa_individus = PriorityQueue()

        # Generam una població
        for i in range(100):
            individu=Individu(percep[ClauPercepcio.POSICIO]['Xavier'],None)
            individu.genera_moviments(20,percep)
            coa_individus.put((individu.calcula_fitness(percep), individu))


        
        while not self.__accions:
            top_10=[]
            for i in range (10):
                _, ind=coa_individus.get()
                # Si ja tenim una solució, deixa de cercar
                if ind.ha_arribat(percep) and ind.es_legal_sempre(percep):
                    self.__accions=ind.accions
                    break
                top_10.append(ind)
            if self.__accions:
                break
            
            # Fer que el top_10 tenguin fills entre ells
            coa_individus=PriorityQueue()
            fills=[]
            for _ in range(5):
                fills.append(top_10.pop().offspring(top_10.pop(),20,percep))
            
            for _ in range(len(fills)):
                ind=fills.pop()
                coa_individus.put((ind.calcula_fitness(percep), ind))
    



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
        # Per prevenir errors
        if accions is None:
            self.__accions=[]
    
    def __lt__(self, other):
        return False
        
    def ha_arribat(self,percep)->bool:
        return (self.__pos_final[0]==percep[ClauPercepcio.OLOR][0]) and (self.__pos_final[1]==percep[ClauPercepcio.OLOR][1])
    
    def __str__(self) -> str:
        return "pos_inicial: "+str(self.__pos_inicial)+" accions: "+str(self.__accions)


    # Comprova si el recorregut que fa una Rana és sempre legal (útil per comprovar si un fill que ha mutat segueix sent legal i per actualitzar la seva posició final)
    def es_legal_sempre(self, percep):
        accions=self.__accions.copy()
        self.__pos_final=self.__pos_inicial

        while accions:
            a=accions.pop()
            if not self.es_legal(a,percep):
                return False


        return True

    # Donada una acció sobre una rana mira si és legal (no se surt del mapa, no se fica dins una paret) i actualitza __pos_final
    def es_legal(self,accio, percep):
        if accio==AccionsRana.ESPERAR:
            return True
        if accio[0]==AccionsRana.MOURE:
            if accio[1]==Direccio.DRETA:
                if self.__pos_final[0]+1>percep[ClauPercepcio.MIDA_TAULELL][0] or (self.__pos_final[0]+1,self.__pos_final[1]) in percep[ClauPercepcio.PARETS]:
                    return False
                self.__pos_final=(self.__pos_final[0]+1,self.__pos_final[1])
            if accio[1]==Direccio.ESQUERRE:
                if self.__pos_final[0]-1<0 or (self.__pos_final[0]-1,self.__pos_final[1]) in percep[ClauPercepcio.PARETS]:
                    return False
                self.__pos_final=(self.__pos_final[0]-1,self.__pos_final[1])
            if accio[1]==Direccio.DALT:
                if self.__pos_final[1]-1<0 or (self.__pos_final[0],self.__pos_final[1]-1) in percep[ClauPercepcio.PARETS]:
                    return False
                self.__pos_final=(self.__pos_final[0],self.__pos_final[1]-1)
            if accio[1]==Direccio.BAIX:
                if self.__pos_final[1]+1>percep[ClauPercepcio.MIDA_TAULELL][0] or (self.__pos_final[0],self.__pos_final[1]+1) in percep[ClauPercepcio.PARETS]:
                    return False
                self.__pos_final=(self.__pos_final[0],self.__pos_final[1]+1)
        else:
            if accio[1]==Direccio.DRETA:
                if self.__pos_final[0]+2>percep[ClauPercepcio.MIDA_TAULELL][0] or (self.__pos_final[0]+2,self.__pos_final[1]) in percep[ClauPercepcio.PARETS]:
                    return False
                self.__pos_final=(self.__pos_final[0]+2,self.__pos_final[1])
            if accio[1]==Direccio.ESQUERRE:
                if self.__pos_final[0]-2<0 or (self.__pos_final[0]-2,self.__pos_final[1]) in percep[ClauPercepcio.PARETS]:
                    return False
                self.__pos_final=(self.__pos_final[0]-2,self.__pos_final[1])
            if accio[1]==Direccio.DALT:
                if self.__pos_final[1]-2<0 or (self.__pos_final[0],self.__pos_final[1]-2) in percep[ClauPercepcio.PARETS]:
                    return False
                self.__pos_final=(self.__pos_final[0],self.__pos_final[1]-2)
            if accio[1]==Direccio.BAIX:
                if self.__pos_final[1]+2>percep[ClauPercepcio.MIDA_TAULELL][0] or (self.__pos_final[0],self.__pos_final[1]+2) in percep[ClauPercepcio.PARETS]:
                    return False
                self.__pos_final=(self.__pos_final[0],self.__pos_final[1]+2)
        
        return True


    @property
    def accions(self):
        return self.__accions

    # qt indica quants de moviments vol generar per aquest individu
    def genera_moviments(self, qt:int, percep):
        self.__accions=[]


        for i in range(qt):
            a=self.acc_pos[randint(0,len(self.acc_pos)-1)]
            if self.es_legal(a,percep):
                self.__accions.insert(0,a)
            
            if self.ha_arribat(percep):
                break
    


    def calcula_fitness(self, percep):
        fitness=0
        # Distància Manhattan a sa pizza
        fitness= abs(percep[ClauPercepcio.OLOR][0]-self.__pos_final[0])+abs(percep[ClauPercepcio.OLOR][1]-self.__pos_final[1])
        if not self.es_legal_sempre(percep):
            return 10000000

        # Penalitzam fer moviments inútils
        # 80% distància manhattan 20% quantitat de moviments
        fitness=80*fitness+20*len(self.__accions)


        return fitness

    def muta(self, percep):
        # sel·lecciona un moviment aleatori 
        idx = randint(0,len(self.__accions)-1)

        # canvia aquest moviment per un altre moviment aleatori
        nova_acc=randint(0,len(self.acc_pos)-1)
        self.__accions[idx]=nova_acc

    # Genera fills entre dos individus i retorna la seva descendènica
    def offspring(self, other, qt:int, percep) -> tuple:
        fills=[]

        for i in range(qt):
            pare_dominant=choice([True,False])
            fill = Individu((percep[ClauPercepcio.POSICIO]['Xavier'][0],percep[ClauPercepcio.POSICIO]['Xavier'][1]),None)

            # Seleccionar 'a' primers moviments de pare (self) + 'b' darrers moviments de mare (other)
            if pare_dominant:
                a=randint(1,len(self.__accions)-1)
                b=randint(1,len(other.accions)-1)
                b=len(other.accions)-1-b
                
                # fica ses 'a' primeres accions del pare
                for j in range(a):
                    if fill.es_legal(a, percep):
                        fill.accions.insert(0,self.__accions[j])
                # fica ses 'b' darreres accions de la mare
                while b<len(other.accions)-1:
                    if fill.es_legal(other.accions[b],percep):
                        fill.accions.insert(0,other.accions[b])
                        # Si ja ha arribat a la pizza, deixa de ficar accions
                        if fill.ha_arribat(percep):
                            break
                    else:
                        break
                    b=b+1

            # Seleccionar 'a' primers moviments de pare (other) + 'b' darrers moviments de mare (self)
            else:
                a=randint(1,len(self.__accions)-1)
                b=randint(1,len(other.accions)-1)
                b=len(other.accions)-1-b
                
                fill = Individu(percep[ClauPercepcio.POSICIO]['Xavier'],None)
                # fica ses 'a' primeres accions del pare
                for j in range(b):
                    fill.accions.insert(0,other.accions[j])
                # fice ses 'b' darreres accions de la mare
                while a<len(self.__accions)-1:
                    if fill.es_legal(self.__accions[a],percep):
                        fill.accions.insert(0,self.__accions[a])
                        # Si ja ha arribat a la pizza, deixa de ficar accions
                        if fill.ha_arribat(percep):
                            break
                    else:
                        break
                    a=a+1
            
            # 1% de probabilitats de tenir una mutació
            prob_mutar=randint(0,100)
            if prob_mutar<=1:
                fill.muta(percep)
                # Si el fill no fa un recorregut legal, és executat públicament
                if fill.es_legal_sempre(percep):
                    fills.append(fill)
            else:
                fills.append(fill)
            fills.append(fill)
        return fills