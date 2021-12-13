from noeud_bin import *
from file import *

class Arbre_bin:

    def __init__(self,racine):
        self.racine=racine

    def Parcours_infixe(self,noeud):
        if noeud is not None:
            self.Parcours_infixe(noeud.fgauche)
            print(noeud.contenu)
            self.Parcours_infixe(noeud.fdroit)

    def Parcours_prefixe(self,noeud):
        if noeud is not None:
            print(noeud.contenu)
            self.Parcours_prefixe(noeud.fgauche)
            self.Parcours_prefixe(noeud.fdroit)

    def Parcours_suffixe(self,noeud):
        if noeud is not None:
            self.Parcours_suffixe(noeud.fgauche)
            self.Parcours_suffixe(noeud.fdroit)
            print(noeud.contenu)

    def Parcours_largeur(self,noeud):
        file = File()
        file.enfiler(noeud)
        while not file.est_vide():
            n = file.defiler()
            print(n.contenu)
            if n.fgauche is not None:
                file.enfiler(n.fgauche)
            if n.fdroit is not None:
                file.enfiler(n.fdroit)



if __name__=="__main__":
    a = Arbre_bin(Noeud_bin('A',Noeud_bin('B',Noeud_bin('C',None,Noeud_bin('E')),Noeud_bin('D')),Noeud_bin('F',Noeud_bin('G',Noeud_bin('I'),None),Noeud_bin('H',None,Noeud_bin('J')))))
    # a.Parcours_infixe(a.racine)
    a.Parcours_prefixe(a.racine)
    # a.Parcours_suffixe(a.racine)
    # a.Parcours_largeur(a.racine)