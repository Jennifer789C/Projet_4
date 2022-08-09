"""Définition du contrôleur"""

import datetime
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

    def saisir_resultat_match(self, match):
        """Ajoute le score du match au score total du joueur"""
        self.vue.saisir_resultats_match(match)
        match.joueur1.score += match.resultatJ1[1]
        match.joueur2.score += match.resultatJ2[1]

    def commencer(self):
        """Commence le tournoi"""
        self.vue.entrer_joueurs()
        self.saisir_joueurs()
        self.vue.commencer_tour()

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

        self.vue.declarer_fin_tour()
        tour1.date_heure_fin = datetime.datetime.now()
        self.tournoi.tournees.append(tour1)

        self.saisir_resultat_match(tour1.match1)
        rencontre = (tour1.match1.joueur1, tour1.match1.joueur2)
        self.tournoi.rencontres.append(rencontre)

        self.saisir_resultat_match(tour1.match2)
        rencontre = (tour1.match2.joueur1, tour1.match2.joueur2)
        self.tournoi.rencontres.append(rencontre)

        self.saisir_resultat_match(tour1.match3)
        rencontre = (tour1.match3.joueur1, tour1.match3.joueur2)
        self.tournoi.rencontres.append(rencontre)

        self.saisir_resultat_match(tour1.match4)
        rencontre = (tour1.match4.joueur1, tour1.match4.joueur2)
        self.tournoi.rencontres.append(rencontre)

        self.vue.commencer_tour()

        # Tri des joueurs par score puis par classement
        tournoi.joueurs.sort(key=lambda joueur: joueur.classement)
        tournoi.joueurs.sort(key=lambda joueur: joueur.score, reverse=True)
