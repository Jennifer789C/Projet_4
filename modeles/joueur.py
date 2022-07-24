"""Définition d'un joueur"""


class Joueur:
    """Un joueur est une personne avec une identité propre et un classement"""
    def __init__(self, nom, prenom, date_naissance, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement

    def __str__(self):
        return f"{self.prenom} {self.nom} né le {self.date_naissance.day}/{self.date_naissance.month}/" \
               f"{self.date_naissance.year} est classé {self.classement}e."
