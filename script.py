from controleurs.controleur import Controleur
from vues.vue import Vue


def main():
    vue = Vue()
    jeu = Controleur(vue)
    jeu.commencer()


main()
"""
Possibilité d'avoir plus ou moins de 8 joueurs ???
gestion des erreurs : un classement déjà attribué à un joueur

Générer les paires du tour 2
"""