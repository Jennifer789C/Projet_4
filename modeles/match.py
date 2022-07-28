"""Définition d'un match"""

from modeles.joueur import Joueur


class Match:
    """Un match se compose de 2 joueurs et un résultat chacun"""
    def __init__(self, joueur1, joueur2):
        """Initialise les joueurs et les résultats"""
        score = 0.0
        self.joueur1 = joueur1
        joueur1 = [Joueur, score]
        self.joueur2 = joueur2
        joueur2 = [Joueur, score]
        self.match = (joueur1, joueur2)

    def __str__(self):
        return f"{self.joueur1} joue contre {self.joueur2}"
