"""Définition d'un tour"""
import datetime


class Tour:
    """Un tour est une liste de matchs"""
    def __init__(self, nom, match1, match2, match3, match4):
        """Initialise le nom du tour, la liste des matchs et le moment du début du tour"""
        super().__init__()
        self.nom = nom
        self.match1 = match1
        self.match2 = match2
        self.match3 = match3
        self.match4 = match4
        self.tour = [match1, match2, match3, match4]
        self.date_heure_debut = datetime.datetime.now()
        self.date_heure_fin = datetime.datetime.now()

    def __str__(self):
        return f"{self.nom} :\n {self.match1} \n {self.match2} \n {self.match3} \n {self.match4}"
