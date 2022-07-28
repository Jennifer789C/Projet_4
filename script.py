from controleurs.controleur import Controleur
from vues.vue import Vue


def main():
    vue = Vue()
    jeu = Controleur(vue)
    jeu.commencer()


main()
"""
Possibilité d'avoir plus ou moins de 8 joueurs ???

Ajouter le tour 1 dans la liste des tournées du tournoi
Fin du tour :   vue : saisir la fin du tour
                modèle tour : intégration de la donnée date_heure_fin

Saisie des scores de chaque joueur
"""