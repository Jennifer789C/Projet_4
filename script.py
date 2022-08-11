from controleurs.controleur import Controleur


def main():
    jeu = Controleur()
    jeu.commencer()


main()
"""
Possibilité d'avoir plus ou moins de 8 joueurs ???
gestion des erreurs : un classement déjà attribué à un joueur
gestion des erreurs : si rien n'est renseigné pour le nom ou le prénom du joueur
gestion des erreurs : si rien n'est renseigné pour le nom et le lieu du tournoi

Intégrer le package TinyDB
"""