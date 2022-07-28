from controleurs.controleur import Controleur
from vues.vue import Vue


def main():
    vue = Vue()
    jeu = Controleur(vue)
    jeu.commencer()


main()
"""
Possibilité d'avoir plus ou moins de 8 joueurs ???
Génération des paires de joueurs pour le tour 1 :
 => Création du tour 1 et de ses 4 matchs

Afficher les paires du tour
"""