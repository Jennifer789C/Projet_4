"""Définition du contrôleur"""

import datetime
from tinydb import TinyDB
from modeles.tournoi import Tournoi
from modeles.tour import Tour
from modeles.match import Match
from modeles.joueur import Joueur
from vues.vue import Vue
from vues.menu import Menu

JOUEURS_MAX = 8


class Controleur:
    """Un contrôleur a un tournoi, une vue utilisateur, un menu principal et une base de données"""
    def __init__(self):
        """Initialise les vues, le modèle et la base de données"""
        # vue
        self.vue = Vue()
        self.menu = Menu()
        # modèle
        self.tournoi = self.creer_tournoi()
        # base de données : contient une table joueurs et une table tournois
        bdd = TinyDB("base_de_données.json")
        self.table_joueurs = bdd.table("joueurs")
        self.table_tournois = bdd.table("tournois")

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
        joueurs_serialises = []
        while len(self.tournoi.joueurs) < JOUEURS_MAX:
            donnees = self.vue.saisir_donnees_joueurs()
            joueur = Joueur(donnees["nom"], donnees["prenom"], donnees["date_naissance"], donnees["sexe"], donnees["classement"])
            self.tournoi.joueurs.append(joueur)
            date_naissance = str(joueur.date_naissance)
            joueur_serialise = {"nom": joueur.nom, "prenom": joueur.prenom, "date_naissance": date_naissance,
                                "sexe": joueur.sexe, "classement": joueur.classement}
            joueurs_serialises.append(joueur_serialise)
        return joueurs_serialises

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

    def serialiser_tournoi(self, tournoi):
        """Sérialise le tournoi pour l'ajouter à la base de données"""
        date_debut = str(tournoi.date_debut)
        date_fin = str(tournoi.date_fin)
        joueurs_tournoi = []
        for participant in tournoi.joueurs:
            date_naissance = str(participant.date_naissance)
            personne = {"nom": participant.nom, "prenom": participant.prenom, "date_naissance": date_naissance,
                        "sexe": participant.sexe,
                        "classement": participant.classement}
            joueurs_tournoi.append(personne)

        tournees = []
        for partie in tournoi.tournees:
            matchs = [partie.match1, partie.match2, partie.match3, partie.match4]
            rencontres = []

            for match in matchs:
                date_naissance1 = str(match.joueur1.date_naissance)
                joueur1 = {"nom": match.joueur1.nom, "prenom": match.joueur1.prenom, "date_naissance": date_naissance1,
                           "sexe": match.joueur1.sexe, "classement": match.joueur1.classement}
                score1 = match.score1
                resultatJ1 = [joueur1, score1]
                date_naissance2 = str(match.joueur2.date_naissance)
                joueur2 = {"nom": match.joueur2.nom, "prenom": match.joueur2.prenom, "date_naissance": date_naissance2,
                           "sexe": match.joueur2.sexe, "classement": match.joueur2.classement}
                score2 = partie.match1.score2
                resultatJ2 = [joueur2, score2]
                rencontre = (resultatJ1, resultatJ2)
                rencontres.append(rencontre)

            date_heure_debut = str(partie.date_heure_debut)
            date_heure_fin = str(partie.date_heure_fin)
            jeu = {"nom": partie.nom, "matchs": rencontres, "date_heure_debut": date_heure_debut, "date_heure_fin": date_heure_fin}
            tournees.append(jeu)

        tournoi_serialise = {"nom": tournoi.nom, "lieu": tournoi.lieu, "date_debut": date_debut, "date_fin": date_fin,
                             "temps": tournoi.temps, "description": tournoi.description, "nb_tours": tournoi.nb_tours,
                             "joueurs": joueurs_tournoi, "tournees": tournees}

        return tournoi_serialise

    def afficher_rapports(self):
        """Interagit avec le système en fonction des choix de l'utilisateur"""
        choix = self.menu.choix_rapport()
        if choix == "1":
            for row in self.table_joueurs:
                self.menu.afficher_rapport(row)

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
            for row in self.table_tournois:
                self.menu.afficher_rapport(row)

        if choix == "4":
            self.menu.afficher_rapport(self.tournoi.tournees)

        if choix == "5":
            self.menu.afficher_rapport(self.tournoi.rencontres)

        if choix == "6":
            self.menu.afficher_menu_principal()
            exit()

    def menu_principal(self):
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
                    joueurs = self.saisir_joueurs()
                    self.table_joueurs.insert_multiple(joueurs)

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
                        tournoi_serialise = self.serialiser_tournoi(self.tournoi)
                        self.table_tournois.insert(tournoi_serialise)

            if choix == "3":
                self.saisir_nouveaux_classements(self.tournoi.joueurs)

            if choix == "4":
                self.afficher_rapports()

            if choix == "5":
                exit()
                return False
