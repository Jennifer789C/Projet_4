"""Définition du contrôleur"""

from modeles.tournoi import Tournoi
from modeles.tour import Tour
from modeles.match import Match
from modeles.joueur import Joueur
from vues.vue import Vue


class Controleur:
    """Un contrôleur a un tournoi et une vue"""
    def __init__(self, vue: Vue):
        """Initialise la vue et les modèles"""
        # vue
        self.vue = vue
        # modèles
        self.tournoi = self.creer_tournoi()

    def creer_tournoi(self):
        """Crée un tournoi"""
        infos = self.vue.saisie_infos_tournoi()
        if "nb_tours" in infos:
            tournoi = Tournoi(infos["nom"], infos["lieu"], infos["date_debut"], infos["date_fin"], infos["temps"],
                              infos["description"], infos["nb_tours"])
        else:
            tournoi = Tournoi(infos["nom"], infos["lieu"], infos["date_debut"], infos["date_fin"], infos["temps"],
                              infos["description"])

        return tournoi

    def saisir_joueurs(self):
        """Crée la liste de joueurs"""
        joueurs_max = 8
        while len(self.tournoi.joueurs) < joueurs_max:
            donnees = self.vue.saisie_donnees_joueurs()
            joueur = Joueur(donnees["nom"], donnees["prenom"], donnees["date_naissance"], donnees["sexe"], donnees["classement"])
            self.tournoi.joueurs.append(joueur)

    def generer_paires_tour_1(self):
        """Crée les paires de joueurs pour le premier tour"""


        return tour1

    def commencer(self):
        """Commence le tournoi"""
        self.vue.entrer_joueurs()
        self.saisir_joueurs()
        self.vue.lancer_generation_paires()

        # Tri des joueurs par classement
        self.tournoi.joueurs.sort(key=lambda joueur: joueur.classement)

        # Division des joueurs en 2 groupes pour créer les matchs du tour 1
        nb_joueurs = len(self.tournoi.joueurs)
        moitie = nb_joueurs // 2
        joueurs_moitie_sup = self.tournoi.joueurs[:moitie]
        joueurs_moitie_inf = self.tournoi.joueurs[moitie:]

        match1 = Match(joueurs_moitie_sup[0], joueurs_moitie_inf[0])
        match2 = Match(joueurs_moitie_sup[1], joueurs_moitie_inf[1])
        match3 = Match(joueurs_moitie_sup[2], joueurs_moitie_inf[2])
        match4 = Match(joueurs_moitie_sup[3], joueurs_moitie_inf[3])

        tour1 = Tour("Round 1", match1, match2, match3, match4)

        self.vue.afficher_paires_joueurs(tour1)
