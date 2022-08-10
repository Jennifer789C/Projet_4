from modeles.tournoi import Tournoi
from modeles.joueur import Joueur
from modeles.match import Match
from modeles.tour import Tour

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
rencontre1 = (bebe, toi)   # bebe gagne
tournoi.rencontres.append(rencontre1)
match2 = Match(mimi, maman)
rencontre2 = (mimi, maman)   # égalité
tournoi.rencontres.append(rencontre2)
match3 = Match(chou, moi)
rencontre3 = (chou, moi)   # moi gagne
tournoi.rencontres.append(rencontre3)
match4 = Match(nani, papa)
rencontre4 = (nani, papa)   # égalité
tournoi.rencontres.append(rencontre4)
tour1 = Tour("Round 1", match1, match2, match3, match4)
tournoi.tournees.append(tour1)
"""
# tour 2 :
rencontre5 = (bebe, moi)   # bebe gagne
tournoi.rencontres.append(rencontre5)
rencontre6 = (mimi, nani)   # nani gagne
tournoi.rencontres.append(rencontre6)
rencontre7 = (maman, papa)   # égalité
tournoi.rencontres.append(rencontre7)
rencontre8 = (chou, toi)   # chou gagne
tournoi.rencontres.append(rencontre8)

# tour 3 :
rencontre9 = (bebe, nani)   # bebe gagne
tournoi.rencontres.append(rencontre9)
rencontre10 = (chou, maman)   # égalité
tournoi.rencontres.append(rencontre10)
rencontre11 = (moi, papa)   # moi gagne
tournoi.rencontres.append(rencontre11)
rencontre12 = (mimi, toi)   # mimi gagne
tournoi.rencontres.append(rencontre12)
"""
bebe.score = 1.0
mimi.score = 0.5
chou.score = 0.0
nani.score = 0.5
toi.score = 0.0
maman.score = 0.5
moi.score = 1.0
papa.score = 0.5

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
