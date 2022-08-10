"""Définition de la vue contenant le menu principal"""

from .vue import Vue


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
        choix = input("Que voulez-vous faire ? (Veuillez saisir l'indice du point de menu) ")
        print()
        while choix != "1" and choix != "2" and choix != "3" and choix != "4":
            print("Veuillez indiquer le numéro du point de menu")
            choix = input("Que voulez-vous faire ? ")
            print()
        return choix

    def erreur_choix(self):
        """Indique à l'utilisateur qu'il ne peut pas choisir ces points de menu"""
        print("Vous devez saisir des joueurs dans un premier temps")

    def afficher_rapports(self):
        """Affiche la liste des rapports disponibles"""
        print("Rapports")
        print("1. Liste des acteurs")
        print("2. Liste des joueurs")
        print("3. Liste des tournois")
        print("4. Liste des tours")
        print("5. Liste des matchs")
        print("6. Retour au menu principal")
        choix = input("Que voulez-vous faire ? (Veuillez saisir l'indice du point de menu) ")
        print()
        while choix != "1" and choix != "2" and choix != "3" and choix != "4" and choix != "5" and choix != "6":
            print("Veuillez indiquer le numéro du point de menu")
            choix = input("Que voulez-vous faire ? ")
            print()
        return choix
