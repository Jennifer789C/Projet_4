# OpenClassRooms - Python - Projet 4 : Tournoi d'échecs

Ce projet consiste à élaborer un programme pour un club d'échecs afin de gérer l'ensemble d'un tournoi :
	- la gestion des joueurs,
	- la génération automatique des paires de joueurs pour chaque match,
	- la gestion des résultats de chaque tour,
	- la production de rapports,
	- l'utilisation d'une base de données.

## Application du script

A partir du terminal, se placer dans le répertoire souhaité

### 1. Récupérer le repository GitHub

Cloner le repository GitHub :
```bash
git clone https://github.com/Jennifer789C/Projet_4.git
```
Puis se placer dans le répertoire du projet :
```bash
cd Projet_4
```

### 2. Créer un environnement virtuel et l'activer

*Pour ma part, je travaille sous Windows et avec l'IDE PyCharm, la création d'un environnement virtuel se fait via les paramètres de l'IDE*

Depuis un terminal sous Windows :
```bash
python -m venv env
env/Scripts/activate
```

Depuis un terminal sous Linux ou Mac :
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Installer et lancer le script

Installer les packages du requirements.txt :
```bash
pip install -r requirements.txt
```
Lancer le script python :

Depuis un terminal sous Windows :
```bash
python script.py
```

Depuis un terminal sous Linux ou Mac :
```bash
python3 script.py
```

### 4. Générer un nouveau rapport flake8

Pour générer un nouveau rapport HTML avec Flake8 :
```bash
flake8 --exclude=env --max-line-length 119 --format=html --htmldir=flake8_rapport
```


