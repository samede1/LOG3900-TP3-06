# Description du module server
Le module server comprend l'ensemble des fichiers du backend, ainsi que le module de tests. 

## Répertoires et fichiers
Le module a 2 fichiers de logique métier: operators.py et app.py. Le fichier operators.py comprend des fonctions de calcul arithmétique à 2 opérateurs utilisées par le fichier principal app.py dans le calcul. Le fichier app.py permet également de traiter les requêtes HTTP GET et POST reçue du client. 
Le module de tests sous le répertoire "/tests" est également présent dans server. 


## Dépendances et exécution
La dépendance centrale du module est la bibliothèque Frask. 
Pour exécuter le code du backend et démarrer le serveur Frask (essentiel poour afficher l'interface utilisateur), il faut effectuer la commande suivante : 
    - python app.py

