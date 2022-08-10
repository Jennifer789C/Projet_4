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
        infos = self.vue.saisir_infos_tournoi()
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
            donnees = self.vue.saisir_donnees_joueurs()
            joueur = Joueur(donnees["nom"], donnees["prenom"], donnees["date_naissance"], donnees["sexe"], donnees["classement"])
            self.tournoi.joueurs.append(joueur)

    def saisir_resultat_match(self, match):
        """Ajoute le score du match au score total du joueur"""
        resultat = self.vue.saisir_resultats_match(match)
        if resultat == "0":
            match.resultatJ1[1] = 0.5
            match.resultatJ2[1] = 0.5
        elif resultat == "1":
            match.resultatJ1[1] = 1
            match.resultatJ2[1] = 0
        elif resultat == "2":
            match.resultatJ1[1] = 0
            match.resultatJ2[1] = 1

        match.joueur1.score += match.resultatJ1[1]
        match.joueur2.score += match.resultatJ2[1]

    def generer_paires(self, concurrents):
        """Génère les paires de joueurs pour les matchs d'un tour, à partir du deuxième tour"""
        matchs = []
        while len(concurrents) >= 2:
            premier = concurrents.pop(0)
            for candidat in concurrents:
                test1 = (premier, candidat) not in self.tournoi.rencontres
                test2 = (candidat, premier) not in self.tournoi.rencontres
                if (test1 is True) and (test2 is True):
                    match = Match(premier, candidat)
                    matchs.append(match)
                    concurrents.remove(candidat)
                    break
        return matchs

    def saisir_nouveaux_classements(self, joueurs):
        """Modifie le classement des joueurs"""
        for joueur in joueurs:
            classement = self.vue.saisir_nouveau_classement(joueur)
            joueur.classement = classement

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

        while len(self.tournoi.tournees) < self.tournoi.nb_tours:
            self.vue.commencer_tour()

            # Tri des joueurs par score puis par classement
            self.tournoi.joueurs.sort(key=lambda joueur: joueur.classement)
            self.tournoi.joueurs.sort(key=lambda joueur: joueur.score, reverse=True)

            matchs = self.generer_paires(list(self.tournoi.joueurs))

            numero_round = len(self.tournoi.tournees) + 1
            tour = Tour(f"Round {numero_round}", matchs[0], matchs[1], matchs[2], matchs[3])
            self.vue.afficher_paires_joueurs(tour)

            self.vue.declarer_fin_tour()
            tour.date_heure_fin = datetime.datetime.now()
            self.tournoi.tournees.append(tour)

            self.saisir_resultat_match(tour.match1)
            rencontre = (tour.match1.joueur1, tour.match1.joueur2)
            self.tournoi.rencontres.append(rencontre)

            self.saisir_resultat_match(tour.match2)
            rencontre = (tour.match2.joueur1, tour.match2.joueur2)
            self.tournoi.rencontres.append(rencontre)

            self.saisir_resultat_match(tour.match3)
            rencontre = (tour.match3.joueur1, tour.match3.joueur2)
            self.tournoi.rencontres.append(rencontre)

            self.saisir_resultat_match(tour.match4)
            rencontre = (tour.match4.joueur1, tour.match4.joueur2)
            self.tournoi.rencontres.append(rencontre)

        self.vue.afficher_resultats(self.tournoi)
        self.vue.modifier_classements()
        self.saisir_nouveaux_classements(self.tournoi.joueurs)
