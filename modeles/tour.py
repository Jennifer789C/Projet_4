"""Définition d'un tour"""

from modeles.match import Match


class Tour(list):
    """Un tour est une liste de matchs"""
    def __init__(self):
        """Initialise la liste de matchs"""
        super().__init__()
        match = Match()
        self.append(match)
