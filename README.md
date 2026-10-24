# À propos du projet 
Nom du projet : LOG3000_TP3
Équipe: 06
Membres: Imène Baba-Aissa et Sarah Medjedoub
Ceci est le dépôt de l'équipe 6 du cours LOG3000 dans le cadre du TP3. Il comporte le code du projet de calculatrice de la startup. Ceci a pour objectif de structurer et de documenter la gesiton de versions de l'équipe de développement de la startup pour en améliorer les processus. 

Le frontend du projet est en HTML et CSS, tandis que son backend est en Python. La bibliothèque Flask est utilisée pour le serveur. 

## Prérequis du projet
Le développement du projet requiert l'installation des dépendances suivantes : 
    - Python 3.11 et Pip
    - Git 2.43

## Installation des prérequis

### Étapes d'installation de Python et Pip
Pour installer Python 3.11 et pip, suivez les instructions suivantes : 
1. Télécharger l'exécutable de la version 3.11 de Python [ici](https://www.python.org/downloads/).
2. Ajouter Python au path selon l'OS utilisé. 
3. Vérifier l'installation de Python et Pip à l'aide de la commande : 
    - python -m pip --version


### Commandes Git 
Pour installer Git (version), suivez les instructions suivantes : 
1. Suivre les étapes d'installation selon l'OS précisées [ici](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. Vérifier l'installation de Git à l'aide de la commande : 
    - git --version


## Installation des dépendances
Pour installer les dépendances du projet il faut d'abord créer un environnement virtuel: 
1. Effectuer la commande suivante dans le terminal à la racine du projet: 
    - python -m venv venv
2. Activer l'environnement selon l'OS. 

Pour installer les dépendances, il faut réaliser les étapes suivantes, toujours à la racine du projet : 
1. Effectuer la commande suivante : 
    - pip install -r requirements.txt
 

## Exécution du projet
Pour exécuter le projet :
1. Démarrer l’application depuis le dossier `server` :
   python app.py
2. Ouvrir l’application dans le navigateur :
   http://127.0.0.1:5000 

Pour utiliser la calculatrice :
1. Saisir une expression
2. Appuyer sur `=` pour obtenir le résultat
3. Appuyer sur `C` pour effacer l’affichage 

## Tests 
Les tests se trouvent dans le dossier `tests/` et sont exécutés avec pytest.

Pour installer pytest :
- python -m pip install pytest

Pour exécuter les tests :
- python -m pytest server/tests -v

## Contribution
### Issues
- Toute tâche ou bogue doit être créé/e en tant qu'issue GitHub.
- Format d'une issue :
    ## Description
    Décrire le problème détecté.

    ## Étapes pour reproduire
    1.
    2.
    3.

    ## Comportement attendu

    ## Comportement observé

    ## Tests associés
    - Fichier :
    - Tests échoués :

    ## Critères d'acceptation
    - [ ] Le bug est corrigé.
    - [ ] Les tests associés énoncés passent.
    - [ ] Aucun problème n'est introduit rétroactivement dans le code par la correction de ce bug.

### Branches
- Une nouvelle branche doit être créée pour chaque issue.
- Pour nommer les branches: 
1. Nouveau feature
    - feature/<nom-de-la-feature>
2. Correction d'un bogue
    - fix/<nom-du-bogue>
3. Ajout de documentation
   - docu/<docu-concernée>

### Pull Requests :
- Tous les changements dans les branches doivent être intégrés sur la branche `main` à travers une pull request (éviter de pousser directement sur `main`).
- Tous les tests disponibles doivent passer avant de créer une pull request.
- Une pull request doit être revue, commentée si nécessaire et acceptée pour être fusionnée avec la branche `main.