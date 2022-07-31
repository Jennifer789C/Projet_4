from modeles.tournoi import Tournoi
from modeles.joueur import Joueur
from modeles.match import Match
from modeles.tour import Tour

tournoi = Tournoi("test", "ici", "2022-07-24", "2022-07-24", "2", "")
moi = Joueur("Cotte", "Jennifer", "1990-08-07", "F", "7")
tournoi.joueurs.append(moi)
toi = Joueur("Cotte", "Matthieu", "1990-11-27", "M", "5")
tournoi.joueurs.append(toi)
bebe = Joueur("Cotte", "Julie", "2019-09-11", "F", "1")
tournoi.joueurs.append(bebe)
mimi = Joueur("Cotte", "Jookie", "2014-07-08", "F", "2")
tournoi.joueurs.append(mimi)
maman = Joueur("Malacain", "Sophie", "1968-05-27", "F", "6")
tournoi.joueurs.append(maman)
papa = Joueur("Malacain", "Gilles", "1964-12-02", "M", "8")
tournoi.joueurs.append(papa)
nani = Joueur("Malacain", "Marine", "1993-09-10", "F", "4")
tournoi.joueurs.append(nani)
chou = Joueur("Malacain", "Charlaine", "1996-08-17", "F", "3")
tournoi.joueurs.append(chou)

tournoi.joueurs.sort(key=lambda joueur: joueur.classement)  # tri des joueurs par classement

"""Division des joueurs en 2 groupes pour créer les matchs"""
nb_joueurs = len(tournoi.joueurs)
moitie = nb_joueurs // 2
joueurs_moitie_sup = tournoi.joueurs[:moitie]
joueurs_moitie_inf = tournoi.joueurs[moitie:]

match1 = Match(joueurs_moitie_sup[0], joueurs_moitie_inf[0])
match2 = Match(joueurs_moitie_sup[1], joueurs_moitie_inf[1])
match3 = Match(joueurs_moitie_sup[2], joueurs_moitie_inf[2])
match4 = Match(joueurs_moitie_sup[3], joueurs_moitie_inf[3])

tour1 = Tour("Round 1", match1, match2, match3, match4)
print(tour1)