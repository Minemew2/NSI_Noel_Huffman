from arbre_bin import *

class Compression_Huffman :
    def __init__(self):
        self.dict_car = {}
        self.tab_frq = []
        self.arbre = None
        self.dict_bin = {}

    def table_frequences(self,texte):
        for car in texte:
            if not car in self.dict_car:
                self.dict_car[car] = 1
            else:
                self.dict_car[car] = self.dict_car[car] + 1
        return self.dict_car

    def permutation(self,tableau,index1,index2) :
        save = tableau[index1]
        tableau[index1] = tableau[index2]
        tableau[index2] = save
        return tableau

    def tri(self,tableau):
        index_candidat = 0
        index_best = 0
        compteur = 1
        while compteur != len(tableau):
            for x in range(compteur,len(tableau)) :
                if tableau[index_candidat][1] > tableau[x][1]:
                    index_candidat = x
            tableau = self.permutation(tableau,index_best,index_candidat)
            index_candidat = compteur
            compteur += 1
            index_best = index_candidat
        
        return tableau


    def table_frequences_rangee(self):
        for car, nbr in self.dict_car.items():
            self.tab_frq.append((car,nbr))
        
        self.tab_frq = self.tri(self.tab_frq)

        return self.tab_frq
        

    def Construire_arbre(self,n1,n2):
        if len(self.tab_frq) <= 2:
            if type(n1) is not Noeud_bin:
                n1 = Noeud_bin(self.tab_frq[0][0])
            od = self.tab_frq[0][1]
            if type(n2) is not Noeud_bin:
                n2 = Noeud_bin(self.tab_frq[1][0])
            ng = self.tab_frq[1][0]
            self.arbre = Arbre_bin(Noeud_bin(None,n2,n1))

        else:
            if type(n1) is not Noeud_bin :
                n1 = Noeud_bin(self.tab_frq[0][0])
            o1 = self.tab_frq[0][1]
            if type(n2) is not Noeud_bin:
                n2 = Noeud_bin(self.tab_frq[1][0])
            o2 = self.tab_frq[1][1]
            n3 = Noeud_bin(None,n2,n1)
            self.tab_frq = self.tab_frq[2:]
            self.tab_frq.insert(0,(n3,o1+o2))
            print(self.tab_frq)
            self.Construire_arbre(self.tab_frq[0][0],self.tab_frq[1][0])

    def  Coder_binaire(self,noeud,bin=""):
        if noeud.est_feuille():
            self.dict_bin[noeud.contenu] = bin
        else:
            self.Coder_binaire(noeud.fgauche,bin+"0")
            self.Coder_binaire(noeud.fdroit,bin+"1")
        

        return self.dict_bin


if __name__=="__main__":
    ch = Compression_Huffman()
    dict = ch.table_frequences("eeaaaapppppddd")
    print(dict)
    print(ch.table_frequences_rangee())
    ch.Construire_arbre(ch.tab_frq[0][0],ch.tab_frq[1][0])
    #ch.arbre.Parcours_largeur(ch.arbre.racine)
    # print(ch.arbre.racine.fgauche.contenu)
    print(ch.Coder_binaire(ch.arbre.racine))


