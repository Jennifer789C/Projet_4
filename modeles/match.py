"""Définition d'un match"""

from modeles.joueur import Joueur


class Match:
    """Un match se compose de 2 joueurs et un résultat chacun"""
    def __init__(self, joueur1, joueur2):
        """Initialise les joueurs et les résultats"""
        score = 0.0
        self.joueur1 = joueur1
        self.score1 = score
        self.resultatJ1 = [joueur1, self.score1]
        self.joueur2 = joueur2
        self.score2 = score
        self.resultatJ2 = [joueur2, self.score2]
        self.match = (self.resultatJ1, self.resultatJ2)

    def __str__(self):
        return f"{self.joueur1} joue contre {self.joueur2}"
