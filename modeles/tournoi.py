"""Definition d'un tournoi"""

from typing import List
from modeles.joueur import Joueur
from modeles.tour import Tour


class Tournoi:
    """Un tournoi est un ensemble de tours avec les mêmes joueurs"""
    def __init__(self, nom, lieu, date_debut, date_fin, temps, description, nb_tours=4):
        """Initialise les données d'un tournoi"""
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.temps = temps  # bullet ou blitz ou coup rapide
        self.description = description
        self.nb_tours = nb_tours
        self.joueurs: List[Joueur] = []
        self.tournees: List[Tour] = []

    def __str__(self):
        return f"tournoi = nom : {self.nom}, lieu : {self.lieu}, date début : {self.date_debut}, date fin : {self.date_fin}, temps :" \
               f" {self.temps}, description : {self.description}, nb_tours : {self.nb_tours}"
