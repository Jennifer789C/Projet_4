"""Définition d'une vue"""

from datetime import date


class Vue:
    """La vue est constituée de toutes les interactions avec l'utilisateur"""
    def saisir_infos_tournoi(self):
        """L'utilisateur saisi les infos du tournoi"""
        infos = {}
        nom = input("Quel est le nom de ce tournoi ? ")
        while nom == "":
            nom = input("Veuillez saisir un nom pour ce tournoi : ")
        infos["nom"] = nom

        lieu = input("Où se déroule ce tournoi ? ")
        while lieu == "":
            lieu = input("Veuillez saisir un nom pour ce tournoi : ")
        infos["lieu"] = lieu

        date_debut = input("Quand se déroule ce tournoi ? (veuillez saisir une date au format AAAA-MM-JJ) ")
        while True:
            try:
                date_debut = date.fromisoformat(date_debut)
                break
            except ValueError:
                date_debut = input("Veuillez saisir une date au format AAAA-MM-JJ : ")
        infos["date_debut"] = date_debut

        date_fin = input("Ce tournoi se déroule-t-il sur plusieurs dates ? Si oui, quelle est la date de fin ? "
                         "(veuillez saisir une date au format AAAA-MM-JJ) ")
        if date_fin == "":
            infos["date_fin"] = date_debut
        else:
            while True:
                try:
                    date_fin = date.fromisoformat(date_fin)
                    break
                except ValueError:
                    date_fin = input("Veuillez saisir une date au format AAAA-MM-JJ : ")
            infos["date_fin"] = date_fin

        choix = input("S'agit-il d'un 1=bullet 2=blitz 3=coup rapide ? ")
        while choix != "1" and choix != "2" and choix != "3":
            choix = input("Veuillez saisir 1 pour un bullet, 2 pour un blitz ou 3 pour un coup rapide : ")
        if choix == "1":
            temps = "bullet"
        elif choix == "2":
            temps = "blitz"
        else:
            temps = "coup rapide"
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

    def saisir_donnees_joueurs(self):
        """L'utilisateur saisi les données de chaque joueur"""
        donnees = {}
        print()
        nom = input("Quel est votre nom de famille ? ")
        while nom == "":
            nom = input("Veuillez saisir un nom : ")
        donnees["nom"] = nom

        prenom = input("Quel est votre prénom ? ")
        while prenom == "":
            prenom = input("Veuillez saisir un prenom : ")
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

    def afficher_paires_joueurs(self, tour):
        """Affiche les paires de joueurs"""
        print(tour.__str__())

    def declarer_fin_tour(self):
        """Demande à l'utilisateur de déclarer le moment où le tour se termine"""
        print()
        input("Ce tour est-il terminé ?")
        return True

    def saisir_resultats_match(self, match):
        """Demande à l'utilisateur de saisir les résultats de chaque match du tour"""
        print()
        print(f"Pour le match : {match}")
        resultat = input(f"Veuillez indiquer le résultat : 0=égalité, 1={match.joueur1} gagne, "
                         f"2={match.joueur2} gagne : ")
        while resultat != "0" and resultat != "1" and resultat != "2":
            print("Veuillez saisir 0 pour une égalité et, 1 ou 2 pour désigner le joueur gagnant")
            resultat = input(f"Veuillez indiquer le résultat : 0=égalité, 1={match.joueur1} gagne, "
                             f"2={match.joueur2} gagne : ")

        return resultat

    def afficher_resultats(self, tournoi):
        """Affiche les scores des joueurs à la fin du tournoi"""
        print()
        print("Félicitations ce tournoi est terminé, voici les résultats :")
        for joueur in tournoi.joueurs:
            print(f"{joueur} a obtenu {joueur.score} points")

    def saisir_nouveau_classement(self, joueur):
        """Demande à l'utilisateur de saisir le nouveau classement du joueur"""
        print(f"{joueur} avait un classement initial : {joueur.classement}")
        classement = input("Quel est son nouveau classement ? ")
        if classement == "":
            classement = joueur.classement
        else:
            while True:
                try:
                    classement = int(classement)
                    break
                except ValueError:
                    print("Veuillez saisir une valeur numérique : un entier positif")
                    classement = input("Quel est son nouveau classement ? ")
            while classement < 0:
                print("Veuillez saisir une valeur numérique : un entier positif")
                classement = input("Quel est son nouveau classement ? ")

        return classement
