## Technologies utilisées

backend :
Django J’ai pris Django car je l’avais déjà utilisé auparavant pour certaines app, je sais que c’est un framework qui est bon pour faire des POC ou des petits projets car rapide et facile à initialiser. Dans un contexte ou nous avions quelques semaines pour produire une application ça me semblait être la meilleure solution pour moi.

frontend :
vuejs J’ai pris Vuejs car je l’avais déjà utilisé au paravant, et les components facilitent le développement. C’est aussi dans une optique de rapidité que j’ai choisi ce framework

déploiement :
docker Pour déployer mon application sur la VM, il m’a fallut l’aide de docker. J’ai donc fais un docker à la root de chaque application, et un docker-compose qui lance les 2 docker.

## Librairies

backend:
Pour django j’ai utilisé la librairie rest_framework, pour faire une api nous somme obligés d’utiliser cette librairie. J’utilise la base de donnée par défaut de django : sqlite3. 
J’ai aussi utilisé les cors librairies de Django, pour que les réponses du serveur puissent être interprétés par le front.

frontend:
j’ai utilisé axios pour les queries API, ayant plus de pratique avec axios qu’avec fetch et sachant que la mise en place d’axios est rapide et facile, c’était une évidence pour moi.
Sinon je n’ai utilisé aucune librairie spécifique au frontend, ni aucun framework autre que Vue ou extension css.

déploiement:
Utilisation de docker, docker-compose et nginx. docker m’a servis au déploiement et nginx à la redirection des requêtes entrantes.

## Cycle du développement

- Analyse :
J’ai déabord analysé le sujet pour en comprendre les tenant et aboutissant. Il fallait faire une application qui aurait la capacité d’utiliser tout les pré-requis du sujet. Au début je suis partis sur la conception d’un blog, bien que compliqué cela me semblait le plus rapide à développer.
Lorsque nous n’étions plus obligés d’utiliser les sessions je me suis dis que mon application n’aurait plus aucun sense et devenait trop compliquée pour les pré-requis. Je suis enfin partis sur une application de bloc-notes. En me disant que cela laissait de larges possibilités de modification et que cette dernière pourrait être anonyme. La gestion des personnes ayant accès aux différentes ressources me parraissait plus simple à faire que avec ma précédente idée de blog.

- Conception : 
En partant de mon idée d’application bloc-note, j’ai commencé par immaginer à quoi pourrait ressembler l’UI avec des croquis.
J’ai ensuite départagé les composants de l’application pour créer les différents components de vue, et imaginé les appels axios qui devront être faits. J’ai ensuite imaginé le modèle qu’aurait une note en base de donnée, elle devrait comprendre un titre, un contenu et un auteur.

- Programmation :
J’ai ensuite commencé à programmer. J’ai commencé par le backend avec django, j’ai créer le modèle de note et les 3 calls api qui peuvent être faits sur la table : créer une note, supprimer une note, récupérer les notes.
J’ai ensuite développé le frontend, en commençant par les input utilisateur et en finissant par les calls axios vers le backend.

- Test :
J’ai testé mon application tout au long de son développement, avec postman. J’ai créer des requêtes postman réutilisables pour plus de simplicité. Je n’ai pas créé de test unitaire n’en ayant pas le temps et n’était pas spécifié dans le sujet.

- Déploiement :
C’est la partie sur laquelle j’ai passé le plus de temps, facilement 12 heures. J’ai d’abord essayé de déployer avec Heroku, j’avais des problèmes car je pense toute mon application (le back et le front) était dans le même repo. Je n’ai pas trouvé de solution à ça j’ai donc décidé d’utiliser une autre service. Je me suis donc tourné vers Azure devTestLabs. 
J’ai déployé une VM et cloné le repo dessus. J’ai ensuite créé deux docker et un docker-compose pour le déploiement. Il m’a fallut aussi créer un serveur proxy nginx pour rediriger les requêtes vers les bonnes applications.

## Plateforme de déploiement

J’ai d’abord essayé de déployer sur Heroku, cela n’a pas fonctionné je m’y suis peut-être mal pris. Je me suis alors intéressé au sites de hosting comme firebase, mais la plus part ne prenaient pas en compte la backend ou ne faisaient pas ce que je voulais.
J’ai finalement opté pour azure. Ayant déjà un compte et une VM avant ce cours cela m’était très accessible. J’ai donc déployé mes applications sur une VM d’azure devTestLabs.
J’ai cloné mon application depuis github et fais fonctionner le docker-compose. Les applications fonctionnant sur deux ports différents sur la même machine j’ai donc du aussi utiliser un serveur proxy dans mon cas nginx.
J’ai donc du mettre en place un serveur proxy nginx pour rediriger l’utilisateur vers la bonne application, les deux étant situées à la même adresse: 20.199.116.69.