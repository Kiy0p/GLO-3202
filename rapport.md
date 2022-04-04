## Technologies utilisées

#### TP1
backend :
Django J’ai pris Django car je l’avais déjà utilisé auparavant pour certaines app, je sais que c’est un framework qui est bon pour faire des POC ou des petits projets car rapide et facile à initialiser. Dans un contexte ou nous avions quelques semaines pour produire une application ça me semblait être la meilleure solution pour moi.

frontend :
vuejs J’ai pris Vuejs car je l’avais déjà utilisé au paravant, et les components facilitent le développement. C’est aussi dans une optique de rapidité que j’ai choisi ce framework

déploiement :
docker Pour déployer mon application sur la VM, il m’a fallut l’aide de docker. J’ai donc fais un docker à la root de chaque application, et un docker-compose qui lance les 2 docker.

#### TP2
backend :
J'ai changé de base de données pour adopter postgresql, une librairie plus professionnelle et de production.

## Librairies

#### TP1
backend:
Pour django j’ai utilisé la librairie rest_framework, pour faire une api nous somme obligés d’utiliser cette librairie. J’utilise la base de donnée par défaut de django : sqlite3. 
J’ai aussi utilisé les cors librairies de Django, pour que les réponses du serveur puissent être interprétés par le front.

frontend:
j’ai utilisé axios pour les queries API, ayant plus de pratique avec axios qu’avec fetch et sachant que la mise en place d’axios est rapide et facile, c’était une évidence pour moi.
Sinon je n’ai utilisé aucune librairie spécifique au frontend, ni aucun framework autre que Vue ou extension css.

déploiement:
Utilisation de docker, docker-compose et nginx. docker m’a servis au déploiement et nginx à la redirection des requêtes entrantes.

#### TP2
backend:
J'ai ajouté la librairie rest_framework, pour utiliser des fonctions de la librairie et indiquer que mon serveur était bien une API. J'ai aussi ajouté rest_framework.authtoken, pour al mise en place des jetons d'authentification.
J'ai changé de base de donnée et j'ai donc du ajouter postgresql.

frontend:
J'ai ajouté vuex qui m'a servis à faire le store de l'application que je détaillerais ensuite. J'ai aussi ajouté la librairie vuex-persistedstate pour sauvegarder le store après un rafraichissement de la page.

déploiement:
RAS.

## Cycle du développement

#### TP1
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

#### TP2
- Analyse :
J'ai déabord analisé le sujet pour savoir ce qu'il fallait ajouter à mon application. Ainsi je m'en suis rendu à ce qu'il faille rajouter l'identification des utilisateurs, le parsing des données fournies, et les autorisations.
- Conception :
En partant de l'idée d'ajouter l'authentification, je me suis rendu compte qu'il fallait aussi que je change plusieurs choses à l'application. Les notes étant identifiées par id d'utilisateur, il faudra changer ça pour qu'à la place elles soient identifiées par compte utilisateur.
- Programmation :
J'ai ensuite commencé à programmer. J'ai commencé par faire le backend avec les routes /api/sign/in, /api/sign/up et /api/sign/out. J'ai ajouté l'authentification aux router et bloqué les appels api vers les endpoints qui nécessitaient une authentification.
Dans le frontend, j'ai ajouté les pages de login et de signup. J'ai aussi rajouté une page 404 not found qui servira si l'url fourni ne corresponds à aucun path.
- Test :
Après avoir fais les routes dans le backend, j'ai fais des calls avec Postman pour m'assurer que tout marchait.
- Déploiement :
Rien à signaler j'ai déployer de la même manière qu'au TP1, la VM et la mise en place des outils était déjà faite il m'a juste suffit de pull le dépot de github.

## Vulnérabilités

backend:
J'utilise un serveur API (django rest) ce qui empêche plusieurs attaques, vu que ce ne sont que des endpoints qui sont exposés.
J'ai essayé d'immuniser mon app contre le cache-control. En effet le token est enregistré dans le localstorage et supprimé lorsque l'utilisateur se déconnecte de l'application. Il est aussi supprimé de la base de donnée lorsque l'utilisateur se déconnect et un nouveau est généré à chaque connexions.
J'utilise une librairie (axios) pour faire les requêtes vers le serveur API, ce sont donc des requêtes pré faites. Cela empêche l'injection SQL.
Django possède une protection contre le XSS nativement.
J'ai fais des parse lorsque l'utilisateur s'enregistre dans l'application. Ainsi, les valeurs sont contrôlées dans le backend et un message d'erreur est envoyé au frontend si une erreur arrive. Ainsi, il y a un regex sur l'email et le mot de passe.
Les utilisateurs n'ont pas le droit d'avoir 2 email ou noms d'utilisateur identiques, Django détecte si 2 utilisateurs sont identiques et je retourne une erreur.
Les utilisateurs ne peuvent pas avoir accès aux routes sécurisées (celles utilisées dans la page Home du front) si ils ne sont pas identifiés avec un token généré lors de l'identification.
La librairie d'authentification à été utilisée pour générer les jetons d'authentificationd demanière sécurisée.

frontend:
J'ai parsé les inputs de l'utilisateur pour m'assurer qu'ils correspondaient avec des trandards de sécurité et qu'ils étaient au bon format. Ainsi, il y a un regex sur l'email et le mot de passe, le même que dans le backend.
J'ai utilisé une librairie vur-router, qui s'occupe de la navigation sur le frontend, pour rendre la navigation plus stable et plus sûre. Ainsi, les balises <a> sont remplacées par les balises <router-link>. C'est aussi cette librairie qui s'occupe d'empêcher les utilisateurs d'accéder à la page Home si ils ne sont pas identifiés.
Pour savoir si ils sont identifiés, j'ai utilisé une autre librairie standard et sécurisée vueX. Cela permet la mise en place d'un store pour connaitre l'état actuel de l'utilisateur. Ainsi à tout moment je peux savoir si il est connecté ou non.
Pour que les données du store ne soient pas perdues lors du rafraichissement de la page, j'ai utilisé une autre librairie appelée vuex-persistedstate. Cela permet de sauvegarder l'état du store même aorès un rafraichissement de la page.
