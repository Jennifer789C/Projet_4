"""Définition d'un match"""

from modeles.joueur import Joueur
from typing import List


class Match(tuple):
    """Un match se compose de 2 joueurs et un résultat chacun"""
    def __init__(self):
        """Initialise les joueurs et les résultats"""
        self.joueurs = List[Joueur]
        self.resultats = List[int]


