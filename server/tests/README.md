# Description du module tests
Le module tests contient les fichiers de tests des fichiers de logique métier du backend compris dans le module "server". Les tests détectent les bogues et valident le comportement attendu de la calculatrice.

## Répertoires et fichiers
Le module a 2 fichiers de tests: "test_app.py" et "test_operators.py".  

## Dépendances et exécution
La dépendance centrale du module est la bibliothèque de tests Pytest. 

Pour installer Pytest (si nécessaire) dans le terminal à la racine du projet, il faut utiliser la commande suivante :
    - python -m pip install pytest

Pour exécuter les tests et afficher leurs résultats dans le terminal, il faut utiliser la commande suivante :
    -  python -m pytest server/tests -v


