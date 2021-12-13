class Noeud_bin:

    def __init__(self,c,fg=None,fd=None,p=None):
        self.contenu = c
        self.fgauche = fg
        self.fdroit = fd
        self.pere = p

    def est_feuille(self):
        if self.fgauche is None and self.fdroit is None:
            return True
        else:
            return False

    def ajouter_fils_droit(self,fd):
        self.fdroit = fd
    
    def ajouter_fils_gauche(self,fg):
        self.fgauche = fg

if __name__ == "__main__":
    nb = Noeud_bin("Noeud de test")
    nd = Noeud_bin("fils droit",None,None,nb)
    ng = Noeud_bin("Fils gauche",None,None,nb)
    assert(nb.est_feuille()) == True
    nb.ajouter_fils_droit(nd)
    nb.ajouter_fils_gauche(ng)
    assert(nd.pere) == nb
    assert(ng.pere) == nb
    assert(nb.est_feuille()) == False
    print("ok")