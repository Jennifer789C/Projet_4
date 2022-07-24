"""Définition du contrôleur"""

from modeles.tournoi import Tournoi
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

    def commencer(self):
        """Commence le tournoi"""
        self.vue.entrer_joueurs()
        self.saisir_joueurs()
        self.vue.lancer_generation_paires()
        self.generer_paires_tour_1()
        self.vue.afficher_paires_joueurs()
