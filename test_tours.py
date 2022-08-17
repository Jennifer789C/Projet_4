from modeles.tournoi import Tournoi
from modeles.joueur import Joueur
from modeles.match import Match
from modeles.tour import Tour
from tinydb import TinyDB

tournoi = Tournoi("test", "ici", "2022-07-24", "2022-07-24", "2", "")
moi = Joueur("Cotte", "Jennifer", "1990-08-07", "F", "7")
tournoi.joueurs.append(moi)
toi = Joueur("Cotte", "Matthieu", "1990-11-27", "H", "5")
tournoi.joueurs.append(toi)
bebe = Joueur("Cotte", "Julie", "2019-09-11", "F", "1")
tournoi.joueurs.append(bebe)
mimi = Joueur("Cotte", "Jookie", "2014-07-08", "F", "2")
tournoi.joueurs.append(mimi)
maman = Joueur("Malacain", "Sophie", "1968-05-27", "F", "6")
tournoi.joueurs.append(maman)
papa = Joueur("Malacain", "Gilles", "1964-12-02", "H", "8")
tournoi.joueurs.append(papa)
nani = Joueur("Malacain", "Marine", "1993-09-10", "F", "4")
tournoi.joueurs.append(nani)
chou = Joueur("Malacain", "Charlaine", "1996-08-17", "F", "3")
tournoi.joueurs.append(chou)

# tour 1 :
match1 = Match(bebe, toi)
duo1 = (bebe, toi)   # bebe gagne
tournoi.rencontres.append(duo1)
match2 = Match(mimi, maman)
duo2 = (mimi, maman)   # égalité
tournoi.rencontres.append(duo2)
match3 = Match(chou, moi)
duo3 = (chou, moi)   # moi gagne
tournoi.rencontres.append(duo3)
match4 = Match(nani, papa)
duo4 = (nani, papa)   # égalité
tournoi.rencontres.append(duo4)
tour1 = Tour("Round 1", match1, match2, match3, match4)
tournoi.tournees.append(tour1)

# tour 2 :
match5 = Match(bebe, moi)
duo5 = (bebe, moi)   # bebe gagne
tournoi.rencontres.append(duo5)
match6 = Match(mimi, nani)
duo6 = (mimi, nani)   # nani gagne
tournoi.rencontres.append(duo6)
match7 = Match(maman, papa)
duo7 = (maman, papa)   # égalité
tournoi.rencontres.append(duo7)
match8 = Match(chou, toi)
duo8 = (chou, toi)   # chou gagne
tournoi.rencontres.append(duo8)
tour2 = Tour("Round 2", match5, match6, match7, match8)
tournoi.tournees.append(tour2)

# tour 3 :
match9 = Match(bebe, nani)
duo9 = (bebe, nani)   # bebe gagne
tournoi.rencontres.append(duo9)
match10 = Match(chou, maman)
duo10 = (chou, maman)   # égalité
tournoi.rencontres.append(duo10)
match11 = Match(moi, papa)
duo11 = (moi, papa)   # moi gagne
tournoi.rencontres.append(duo11)
match12 = Match(mimi, toi)
duo12 = (mimi, toi)   # mimi gagne
tournoi.rencontres.append(duo12)
tour3 = Tour("Round 3", match9, match10, match11, match12)
tournoi.tournees.append(tour3)

# tour 4 :
match13 = Match(bebe, mimi)
duo13 = (bebe, mimi)   # égalité
tournoi.rencontres.append(duo13)
match14 = Match(moi, nani)
duo14 = (moi, nani)   # nani gagne
tournoi.rencontres.append(duo14)
match15 = Match(chou, papa)
duo15 = (chou, papa)   # chou gagne
tournoi.rencontres.append(duo15)
match16 = Match(maman, toi)
duo16 = (maman, toi)   # toi gagne
tournoi.rencontres.append(duo16)
tour4 = Tour("Round 4", match13, match14, match15, match16)
tournoi.tournees.append(tour4)

bebe.score = 3.5
mimi.score = 2.0
chou.score = 2.5
nani.score = 2.5
toi.score = 1.0
maman.score = 1.5
moi.score = 2.0
papa.score = 1.0

while len(tournoi.tournees) < 4:
    # Tri des joueurs par score puis par classement
    tournoi.joueurs.sort(key=lambda joueur: joueur.classement)
    tournoi.joueurs.sort(key=lambda joueur: joueur.score, reverse=True)

    concurrents = list(tournoi.joueurs)
    matchs = []
    while len(concurrents) >= 2:
        premier = concurrents.pop(0)
        for candidat in concurrents:
            test1 = (premier, candidat) not in tournoi.rencontres
            test2 = (candidat, premier) not in tournoi.rencontres
            if (test1 is True) and (test2 is True):
                match = Match(premier, candidat)
                matchs.append(match)
                concurrents.remove(candidat)
                break

    numero_round = len(tournoi.tournees) + 1
    tour = Tour(f"Round {numero_round}", matchs[0], matchs[1], matchs[2], matchs[3])
    print(tour)
    tournoi.tournees.append(tour)

bdd = TinyDB("bdd.json")
table_tournois = bdd.table("tournois")
table_tournois.truncate()
date_debut = str(tournoi.date_debut)
date_fin = str(tournoi.date_fin)
joueurs_tournoi = []
for participant in tournoi.joueurs:
    date_naissance = str(participant.date_naissance)
    personne = {"nom": participant.nom, "prenom": participant.prenom, "date_naissance": date_naissance, "sexe": participant.sexe,
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
table_tournois.insert(tournoi_serialise)
