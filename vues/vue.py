"""Définition d'une vue"""

from datetime import date


class Vue:
    """La vue est constituée de toutes les interactions avec l'utilisateur"""
    def saisie_infos_tournoi(self):
        """L'utilisateur saisi les infos du tournoi"""
        infos = {}
        nom = input("Quel est le nom de ce tournoi ? ")
        infos["nom"] = nom
        lieu = input("Où se déroule ce tournoi ? ")
        infos["lieu"] = lieu

        date_debut = input("Quand se déroule ce tournoi ? (veuillez saisir une date au format AAAA-MM-JJ) ")
        while True:
            try:
                date_debut = date.fromisoformat(date_debut)
                break
            except ValueError:
                print("Veuillez saisir une date au format AAAA-MM-JJ")
                date_debut = input("Quand se déroule ce tournoi ? ")
        infos["date_debut"] = date_debut

        date_fin = input("Ce tournoi se déroule-t-il sur plusieurs dates ? Si oui, quelle est la date de fin ? (veuillez saisir une "
                         "date au format AAAA-MM-JJ) ")
        if date_fin == "":
            infos["date_fin"] = date_debut
        else:
            while True:
                try:
                    date_fin = date.fromisoformat(date_fin)
                    break
                except ValueError:
                    print("Veuillez saisir une date au format AAAA-MM-JJ")
                    date_fin = input("Quelle est la date de fin de ce tournoi ? ")
            infos["date_fin"] = date_fin

        temps = input("S'agit-il d'un 1=bullet 2=blitz 3=coup rapide ? ")
        while temps != "1" and temps != "2" and temps != "3":
            print("Veuillez saisir 1 pour un bullet, 2 pour un blitz ou 3 pour un coup rapide")
            temps = input("S'agit-il d'un 1=bullet 2=blitz 3=coup rapide ? ")
        infos["temps"] = temps

        nb_tours = input("En combien de tours va se passer ce tournoi ? (par défaut, il y en a 4) ")
        if not nb_tours == "":
            infos["nb_tours"] = nb_tours

        description = input("Voulez vous ajouter une description ? ")
        if description == "non":
            infos["description"] = ""
        else:
            infos["description"] = description

        return infos

    def entrer_joueurs(self):
        """Demande à l'utilisateur s'il est prêt à faire entrer les joueurs"""
        print()
        input("Prêt à faire entrer les joueurs ?")
        return True

    def saisie_donnees_joueurs(self):
        """L'utilisateur saisi les données de chaque joueur"""
        donnees = {}
        print()
        nom = input("Quel est votre nom de famille ? ")
        donnees["nom"] = nom
        prenom = input("Quel est votre prénom ? ")
        donnees["prenom"] = prenom

        date_naissance = input("Quelle est votre date de naissance ? (veuillez saisir une date au format AAAA-MM-JJ) ")
        while True:
            try:
                date_naissance = date.fromisoformat(date_naissance)
                break
            except ValueError:
                print("Veuillez saisir une date au format AAAA-MM-JJ")
                date_naissance = input("Quelle est votre date de naissance ? ")
        donnees["date_naissance"] = date_naissance

        sexe = input("De quel sexe êtes-vous ? (H/F) ")
        sexe = sexe.upper()
        while sexe != "H" and sexe != "F":
            print("Veuillez saisir H pour un homme ou F pour une femme")
            sexe = input("De quel sexe êtes-vous ? ")
        donnees["sexe"] = sexe

        classement = input("Quel est votre classement ? ")
        while True:
            try:
                classement = int(classement)
                break
            except ValueError:
                print("Veuillez saisir une valeur numérique : un entier positif")
                classement = input("Quel est votre classement ? ")
        while classement < 0:
            print("Veuillez saisir une valeur numérique : un entier positif")
            classement = input("Quel est votre classement ? ")
        donnees["classement"] = classement

        return donnees

    def lancer_generation_paires(self):
        """Demande à l'utilisateur s'il est prêt à générer les paires de joueurs"""
        print()
        input("Prêt à commencer le tour ?")
        return True

    def afficher_paires_joueurs(self, tour):
        """Affiche les paires de joueurs"""
        print(tour.__str__())

    def declarer_fin_tour(self):
        """Demande à l'utilisateur de déclarer le moment où le tour se termine"""
        print()
        input("Ce tour est-il terminé ?")
        return True

    def saisir_resultats_match(self, tour):
        """Demande à l'utilisateur de saisir les résultats de chaque match du tour"""
        print(f"Pour le match : {tour.match1}")
        input(f"Veuillez indiquer le résultat : 0=égalité, 1={tour.match1.joueur1} gagne, 2={tour.match1.joueur2} gagne : ")
