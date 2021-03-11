# README

Lien de l'app déployé : [https://django-fo.herokuapp.com/](https://django-fo.herokuapp.com/formation)

## Contributeurs

* [Paartheepan RAVEENTHIRAN](https://github.com/Punkte)  
* [Etienne MELA](https://github.com/EtienneMela)  
* [Adrien BANNWARTH](https://github.com/Adrienbannwarth)  

## Application

Notre application formation permet de creer des CV en rensignant notre nom, nos compétences et nos skills.
Après avoir postuler, on peut retrouver le résumé de notre CV.
On a également la possibilité de voir la liste de tous les CV publié sur la plateforme.


Stack utilisés:

- Docker
- Django
- Bootstrap 
- Heroku


## Installation de l'environnement de développement

Pour installer le projet :

```bash
$ make install
```

Cette commande effectue les actions suivantes :
* lance les containers situés dans le fichier [docker-compose.yml](./docker-compose.yml)
* lance les migrations
* crée un super user avec les informations suivantes :
  * username: root
  * password: root

Le projet est lancé sur le port 8080 de la machine hôte.

Pour générer des migrations : 
```bash
$ make generate-migrations
```