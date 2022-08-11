"""Définition de la vue contenant le menu principal"""


class Menu:
    """Le menu est le point d'entrée de la vue utilisateur"""
    def afficher_menu_principal(self):
        """Affiche le menu principal"""
        print()
        print("Menu principal")
        print("1. Ajouter des joueurs")
        print("2. Lancer un tour")
        print("3. Modifier le classement d'un joueur")
        print("4. Sélectionner un rapport")
        print("5. Quitter")
        choix = input("Que voulez-vous faire ? (Veuillez saisir l'indice du point de menu) ")
        print()
        while choix != "1" and choix != "2" and choix != "3" and choix != "4" and choix != "5":
            print("Veuillez indiquer le numéro du point de menu")
            choix = input("Que voulez-vous faire ? ")
            print()
        return choix

    def erreur_choix(self):
        """Indique à l'utilisateur qu'il ne peut pas choisir ces points de menu"""
        print("Vous devez saisir des joueurs dans un premier temps")

    def max_joueurs_atteint(self):
        """Indique à l'utilisateur qu'il a entré le maximum de joueurs"""
        print("Tous les joueurs ont été saisis")

    def choix_rapport(self):
        """Affiche la liste des rapports disponibles"""
        print("Rapports")
        print("1. Liste des acteurs")
        print("2. Liste des joueurs d'un tournoi")
        print("3. Liste des tournois")
        print("4. Liste des tours d'un tournoi")
        print("5. Liste des matchs d'un tournoi")
        print("6. Retour au menu principal")
        choix = input("Que voulez-vous faire ? (Veuillez saisir l'indice du point de menu) ")
        print()
        while choix != "1" and choix != "2" and choix != "3" and choix != "4" and choix != "5" and choix != "6":
            print("Veuillez indiquer le numéro du point de menu")
            choix = input("Que voulez-vous faire ? ")
            print()
        return choix

    def tri_liste(self):
        """Demande à l'utilisateur comment il souhaite trier la liste"""
        resultat = input("Souhaitez-vous trier cette liste par ordre alphabétique (A) ou par classement (C) ? ")
        resultat = resultat.upper()
        while resultat != "A" and resultat != "C":
            resultat = input("Veuillez saisir A pour un tri par ordre alphabétique ou C pour un tri par classement ")
        return resultat

    def afficher_rapport(self, liste):
        """Affiche le rapport choisi par l'utilisateur"""
        print(liste)
