# NSI_Noel_Huffman

## Méthodes :
- **Coder_pseudo_binaire :**  Méthode qui depuis la racine de l’arbre de Huffman construit une liste de couple (caractère,
code binaire sous la forme d’une chaîne de caractère).
- **Coder_binaire :** Méthode qui depuis la liste précédente, construit un dictionnaire ou les clés sont les
caractères et ou la valeur est un couple (valeur_num, taille en bits de valeur_num).
- **Ajouter_texte :** Méthode qui depuis un fichier texte fournit sous moodle met à jour l’attribut texte de la
classe Codage_huffman.
- **Coder_texte :** Méthode codant l’attribut texte en une valeur binaire.
- **Decoder_texte :** Méthode décodant une valeur binaire en un texte en utilisant un arbre de Huffman.
- **Valeur_compression :** Méthode rendant le % de compression entre le texte original et la valeur binaire codée par la
méthode de Huffman.
