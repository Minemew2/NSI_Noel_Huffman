from arbre_bin import *


class Compression_Huffman:
    def __init__(self):
        self.dict_car = {}
        self.tab_frq = []
        self.arbre = None
        self.dict_bin = {}
        self.texte_coder = 0

    def table_frequences(self, texte):
        for car in texte:
            if not car in self.dict_car:
                self.dict_car[car] = 1
            else:
                self.dict_car[car] = self.dict_car[car] + 1
        return self.dict_car

    def permutation(self, tableau, index1, index2):
        save = tableau[index1]
        tableau[index1] = tableau[index2]
        tableau[index2] = save
        return tableau

    def tri(self, tableau):
        index_candidat = 0
        index_best = 0
        compteur = 1
        while compteur != len(tableau):
            for x in range(compteur, len(tableau)):
                if tableau[index_candidat][1] > tableau[x][1]:
                    index_candidat = x
            tableau = self.permutation(tableau, index_best, index_candidat)
            index_candidat = compteur
            compteur += 1
            index_best = index_candidat

        return tableau

    def table_frequences_rangee(self):
        for car, nbr in self.dict_car.items():
            self.tab_frq.append((car, nbr))

        self.tab_frq = self.tri(self.tab_frq)

        return self.tab_frq

    def Construire_arbre(self, n1, n2):
        if len(self.tab_frq) <= 2:
            if type(n1) is not Noeud_bin:
                n1 = Noeud_bin(self.tab_frq[0][0])
            od = self.tab_frq[0][1]
            if type(n2) is not Noeud_bin:
                n2 = Noeud_bin(self.tab_frq[1][0])
            ng = self.tab_frq[1][0]
            self.arbre = Arbre_bin(Noeud_bin(None, n2, n1))

        else:
            if type(n1) is not Noeud_bin:
                n1 = Noeud_bin(self.tab_frq[0][0])
            o1 = self.tab_frq[0][1]
            if type(n2) is not Noeud_bin:
                n2 = Noeud_bin(self.tab_frq[1][0])
            o2 = self.tab_frq[1][1]
            n3 = Noeud_bin(None, n2, n1)
            self.tab_frq = self.tab_frq[2:]
            self.tab_frq.insert(0, (n3, o1 + o2))
            self.Construire_arbre(self.tab_frq[0][0], self.tab_frq[1][0])

    def Coder_pseudo_binaire(self, noeud, bin=""):
        if noeud.est_feuille():
            self.dict_bin[noeud.contenu] = bin
        else:
            self.Coder_pseudo_binaire(noeud.fgauche, bin + "0")
            self.Coder_pseudo_binaire(noeud.fdroit, bin + "1")

        return self.dict_bin

    def Coder_binaire(self, dictionnaire):
        dico_binaire = {}
        for element in dictionnaire.items():
            dico_binaire[element[0]] = (int(element[1], 2), len(element[1]))

        return dico_binaire

    def ajouter_texte(self, fichier):
        texte = open(fichier, "r")
        variable_texte = texte.read()
        return variable_texte

    def coder_texte(self, fichier):
         texte = self.ajouter_texte(fichier)
         self.table_frequences(texte)
         self.table_frequences_rangee()
         self.Construire_arbre(self.tab_frq[0][0], self.tab_frq[1][0])
         self.Coder_pseudo_binaire(self.arbre.racine)
         dico_trie = self.Coder_binaire(self.dict_bin)
         # on ??crit dans le fichier texte avec des vrais nombres
         texte_code = ""
         for x in texte:
             ajout = dico_trie.get(x)
             passage = bin(ajout[0])
             for deux in range(2):
                 passage = passage[1:]
             texte_code += passage
         texte_code = int(texte_code)

         f = open("textecoder.txt", "w+")
         f.truncate(0)  # on efface le contenu du fichier, au cas o?? il y a d??j?? des choses dedans
         f.write("%d" % texte_code)  # c'est du texte, mais la variable texte_code
         # reste compress??

         self.texte_coder += int(texte_code)

         return texte_code

    def Coder_texte(self,str):
        texte = self.ajouter_texte(str)
        self.table_frequences(texte)
        self.table_frequences_rangee()
        self.Construire_arbre(self.tab_frq[0][0], self.tab_frq[1][0])
        self.Coder_pseudo_binaire(self.arbre.racine)
        dico_trie = self.Coder_binaire(self.dict_bin)
        codage_binaire = self.dict_bin[str[0]][0]
        self.first_car = self.dict_bin[str[0]]
        for car in range(1,len(str)):
            codage_binaire = codage_binaire << len(bin(self.dict_bin[str[car]][0]))-2
            codage_binaire = codage_binaire | self.dict_bin[str[car]][0]

        return bin(codage_binaire)

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

    def valeur_compression(self, fichier="texte.txt"):
        f = open(fichier, "r")
        poids_decode = len(f.read())  # en octets
        poids_code = len(str(self.texte_coder))//8  # en octets
        print(poids_code, " VS ", poids_decode)

        print("la valeur de compression est de ", (poids_code/poids_decode)*100, "%")
        return poids_code/poids_decode*100

if __name__ == "__main__":
    # ch = Compression_Huffman()
    # dict = ch.table_frequences("eeaaaapppppddd")
    # print(dict)
    # print(ch.table_frequences_rangee())
    # ch.Construire_arbre(ch.tab_frq[0][0], ch.tab_frq[1][0])
    # ch.arbre.Parcours_largeur(ch.arbre.racine)
    # print(ch.arbre.racine.fgauche.contenu)
    # print(ch.Coder_pseudo_binaire(ch.arbre.racine))
    # print("vrai binaire :")
    # print(ch.Coder_binaire(ch.dict_bin))
    # fichier_texte = ch.ajouter_texte("texte.txt")
    # print(fichier_texte)

    hu = Compression_Huffman()
    print(hu.coder_texte("texte.txt"))
    txtcode = hu.texte_coder
    # f = open("textecoder.txt", "r")
    # print("longueur texte", len(f.read()))
    # print(type(txtcode))
    print("=======d??coder========")
    print(hu.decoder_texte(hu.texte_coder))
    print("=======valeur de compression=======")
    print(hu.valeur_compression())
