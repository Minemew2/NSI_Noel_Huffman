from arbre_bin import *

class Compression_Huffman :
    def __init__(self):
        self.dict_car = {}
        self.tab_frq = []
        self.arbre = None
        self.dict_bin = {}
        self.txt = ""
        self.first_car = None

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
            n3 = Noeud_bin(None,n1,n2)
            self.tab_frq = self.tab_frq[2:]
            self.tab_frq.append((n3,o1+o2))
            self.tab_frq = self.tri(self.tab_frq)
            self.Construire_arbre(self.tab_frq[0][0],self.tab_frq[1][0])

    def  Coder_binaire(self,noeud,str_bin=""):
        if noeud.est_feuille():
            codage = int("0b"+str_bin,2)
            self.dict_bin[noeud.contenu] = (codage,len(str_bin))
        else:
            self.Coder_binaire(noeud.fgauche,str_bin+"0")
            self.Coder_binaire(noeud.fdroit,str_bin+"1")
        

        return self.dict_bin

    def Ajouter_texte(self,path):
        file = open(path)
        self.txt = file.read()

        return self.txt

    def Coder_texte(self,str):
        codage_binaire = self.dict_bin[str[0]][0]
        self.first_car = self.dict_bin[str[0]]
        for car in range(1,len(str)):
            codage_binaire = codage_binaire << self.dict_bin[str[car]][1]
            codage_binaire = codage_binaire | self.dict_bin[str[car]][0]

        return codage_binaire

    def decoder_texte(self, fichiercoder):
        f = fichiercoder
        arbre_decode = self.arbre
        noeud = arbre_decode.racine
        texte_decoder = ""
        listetravail = [int(x) for x in str(f)]
        for x in listetravail:
            if x == 0:
                noeud = noeud.fgauche
                if noeud.contenu is not None:
                    if noeud.est_feuille:
                        texte_decoder += noeud.contenu
                        noeud = arbre_decode.racine

            elif x == 1:
                noeud = noeud.fdroit
                if noeud.contenu is not None:
                    if noeud.est_feuille:
                        texte_decoder += noeud.contenu
                        noeud = arbre_decode.racine

        return texte_decoder

    def valeur_compression(self):
        poids_decode = len(self.txt)  # en octets
        poids_code = (len(str(bin(self.Coder_texte(self.txt))))-2)//8  # en octets
        print(poids_code, " VS ", poids_decode)

        print("la valeur de compression est de ", (poids_code/poids_decode)*100, "%")
        return poids_code/poids_decode*100

if __name__=="__main__":
    ch = Compression_Huffman()
    txt = ch.Ajouter_texte("/home/minemew2/Documents/NSI/TAD/Arbre/Compression_Huffman/extrait_proust.txt")
    ch.table_frequences(txt)
    ch.table_frequences_rangee()
    ch.Construire_arbre(ch.tab_frq[0][0],ch.tab_frq[1][0])
    # ch.arbre.Parcours_largeur(ch.arbre.racine)
    # # print(ch.arbre.racine.fgauche.contenu)
    cod_bin = ch.Coder_binaire(ch.arbre.racine)
    codage = ch.Coder_texte(txt)
    print(ch.decoder_texte(int(bin(codage)[1:][1:])))
    print(ch.valeur_compression())