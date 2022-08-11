"""Définition du contrôleur"""

import datetime
from modeles.tournoi import Tournoi
from modeles.tour import Tour
from modeles.match import Match
from modeles.joueur import Joueur
from vues.vue import Vue
from vues.menu import Menu

JOUEURS_MAX = 8


class Controleur:
    """Un contrôleur a un tournoi, un menu et une vue utilisateur"""
    def __init__(self):
        """Initialise les vues et le modèle"""
        # vue
        self.vue = Vue()
        self.menu = Menu()
        # modèle
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
        while len(self.tournoi.joueurs) < JOUEURS_MAX:
            donnees = self.vue.saisir_donnees_joueurs()
            joueur = Joueur(donnees["nom"], donnees["prenom"], donnees["date_naissance"], donnees["sexe"], donnees["classement"])
            self.tournoi.joueurs.append(joueur)

    def generer_paires_tour1(self):
        """Génère les paires de joueurs du premier tour"""
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

        return tour1

    def declarer_fin_tour(self, tour):
        """A la fin, le tournoi est mis à jour :
        Ajoute le tour à la liste Tournées du tournoi
        Invite l'utilisateur à saisir les résultats des matchs
        Ajoute les rencontres à la liste du tournoi"""

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

    def afficher_rapports(self):
        """Interagit avec le système en fonction des choix de l'utilisateur"""
        choix = self.menu.choix_rapport()
        if choix == "1":
            # A gérer avec le package TinyDB
            pass

        if choix == "2":
            if len(self.tournoi.joueurs) == 0:
                self.menu.erreur_choix()
            else:
                tri = self.menu.tri_liste()
                if tri == "A":
                    self.tournoi.joueurs.sort(key=lambda joueur: joueur.prenom)
                    self.tournoi.joueurs.sort(key=lambda joueur: joueur.nom)
                else:
                    self.tournoi.joueurs.sort(key=lambda joueur: joueur.classement)
                self.menu.afficher_rapport(self.tournoi.joueurs)

        if choix == "3":
            self.menu.afficher_rapport(self.tournoi)
            # A améliorer avec le package TinyDB

        if choix == "4":
            self.menu.afficher_rapport(self.tournoi.tournees)

        if choix == "5":
            self.menu.afficher_rapport(self.tournoi.rencontres)

        if choix == "6":
            self.menu.afficher_menu_principal()
            exit()

    def commencer(self):
        """Commence le tournoi"""
        while True:
            choix = self.menu.afficher_menu_principal()
            while len(self.tournoi.joueurs) == 0:
                if choix == "2" or choix == "3":
                    self.menu.erreur_choix()
                    choix = self.menu.afficher_menu_principal()
                elif choix == "1" or choix == "4" or choix == "5":
                    break

            if choix == "1":
                if len(self.tournoi.joueurs) == JOUEURS_MAX:
                    self.menu.max_joueurs_atteint()
                else:
                    self.saisir_joueurs()

            if choix == "2":
                if len(self.tournoi.tournees) == self.tournoi.nb_tours:
                    self.vue.afficher_resultats(self.tournoi)

                elif len(self.tournoi.tournees) == 0:
                    tour1 = self.generer_paires_tour1()
                    self.vue.afficher_paires_joueurs(tour1)
                    self.declarer_fin_tour(tour1)

                else:
                    # Tri des joueurs par score puis par classement
                    self.tournoi.joueurs.sort(key=lambda joueur: joueur.classement)
                    self.tournoi.joueurs.sort(key=lambda joueur: joueur.score, reverse=True)

                    matchs = self.generer_paires(list(self.tournoi.joueurs))

                    numero_round = len(self.tournoi.tournees) + 1
                    tour = Tour(f"Round {numero_round}", matchs[0], matchs[1], matchs[2], matchs[3])
                    self.vue.afficher_paires_joueurs(tour)

                    self.declarer_fin_tour(tour)

                    if numero_round == self.tournoi.nb_tours:
                        self.vue.afficher_resultats(self.tournoi)

            if choix == "3":
                self.saisir_nouveaux_classements(self.tournoi.joueurs)

            if choix == "4":
                self.afficher_rapports()

            if choix == "5":
                exit()
                return False
