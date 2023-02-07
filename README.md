DESCRIPTION: Gestionnaire de Tournoi :

Création de l'environnement virtuel :

Dans votre terminal, accédez au dossier projet_2_OC : Saisissez dans votre terminal : ``cd nom_du_chemin_d_acces``
Si vous recherchez le path de ce chemin, allez dans le dossier projet_04_OC, et dans la barre de recherche du dossier, 
située en haut du dossier, faites un clic gauche pour sélectionner le chemin, puis un clic droit pour copier coller ce chemin
Dans votre terminal, créez un environnement virtuel pour Python, par convention nous appelerons cet environnement : env
Sous Microsoft Windows : ``python -m venv env``
Sous Linux et Mac : ``python3 -m venv env``
Connectez vous à cet environnement virtuel :
Sur un terminal Windows powershell : ``env/Scripts/Activate.ps1``
Sur un terminal Windows invite de commande : ``env/Scripts/activate.bat``
Sur un terminal Linux ou Mac : ``source env/bin/activate``
Vérifiez que vous êtes bien connecté à votre environnement virtuel, au début de la ligne du terminal doit apparaître : (env) 
Si vous désirez vous déconnecter de votre environnement virtuel, saisissez la commande : ``deactivate``
Installez dans votre environnement virtuel les modules attendus pour le bon fonctionnement du script de la pipeline ETL : 
Une fois connecté à votre environnement virtuel saisissez dans votre terminal la commande : ``pip install -r requirements.txt``
Vous pouvez maintenant lancer le processus d'extraction des données en saisissant dans votre terminal :
Sur Microsoft Windows : ``python main.py``
Sur Linux ou Mac : ``python3 main.py``
Pour toute problématique de lancement lié à l'installation de Python ou des Path liés à Microsoft, Mac ou Linux, 
merci de vous référez directement au site officiel de Python : https://www.python.org/downloads/

LICENSE: Application open source

REQUIREMENTS: Python 3.X, modules (merci de consulter le fichier: requirements.txt)