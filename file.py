class File:
    """
    classe définissant une file de type FIFO
    ---
    Attributs :
    file : liste représentant la file
    ---
    Méthodes :
    enfiler : enfile un élément dans la file
    defiler : defile le premier élément arrivé
    est_vide : Booléen, renvoie True si la file est vide, False sinon
    sommet : renvoie le dernier élément entré dans la file
    nombre_elements : retourne le nombre d'éléments de la file
    affiche : affiche les éléments dans la file dans l'ordre du premier arrivé
      au dernier arrivé
    defilage_complet : defile entièrement la file
    """

    def __init__(self):
        self.file = []

    def enfiler(self, element):
        """
      Méthode qui enfile l'élément "element" dans la File, pas de renvoi
      ---
      element : élément quelconque à intégrer à la file
      """
        self.file.append(element)

    def defiler(self):
        """
        Méthode qui supprime le premier élément entré dans la file
        """
        if self.est_vide() is False:
            result = self.file[0]
            del(self.file[0])
            return result


    def est_vide(self):
        """
        Méthode qui permet de savoir si la file est vide ou non
        ---
        renvoie True si elle est vide, False sinon
        """
        resultat = False
        if self.nombre_elements() == 0:
            resultat = True
        return resultat

    def sommet(self):
        return self.file[-1]

    def nombre_elements(self):
        return len(self.file)

    def affiche(self):
        for i in range(self.nombre_elements()):
            print(self.file[i])

    def defilage_complet(self):
        """
        Méthode qui défile tous les éléments de la file
        """
        while self.est_vide() is not True:
            self.defiler()


if __name__ == "__main__":
    F1 = File()
    F1.enfiler("TRIGHT")
    F1.enfiler("TLEFT")
    F1.enfiler("D")
    F1.enfiler("Q")
    assert(F1.nombre_elements() == 4)
    assert(F1.sommet() == "Q")
    F1.defiler()
    assert (F1.nombre_elements() == 3)
    F1.defilage_complet()
    assert(F1.nombre_elements() == 0)