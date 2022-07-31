from controleurs.controleur import Controleur
from vues.vue import Vue


def main():
    vue = Vue()
    jeu = Controleur(vue)
    jeu.commencer()


main()
"""
Possibilité d'avoir plus ou moins de 8 joueurs ???

Intégrer les scores de chaque joueur dans la classe Joueur pour pouvoir les trier pour les prochains tours
Générer les paires du tour 2
"""