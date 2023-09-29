<img width="482" alt="image" src="https://github.com/faycalzaazoua/azureDoc/assets/83638729/53ba4dbe-2bd5-4910-b6da-f0250ea422ba">CUSTOMER SCENARIO

Contexte :

Tech Innovations Ltd. est une start-up en pleine croissance qui a récemment lancé une application de sondage. Leur service a attiré un nombre croissant d'utilisateurs, et ils prévoient un grand sondage en direct très médiatisé qui devrait entraîner un afflux massif d'utilisateurs sur leur plateforme. Cependant, leur infrastructure existante ne peut pas gérer un tel volume de trafic, et ils veulent s'assurer que leur service reste disponible et réactif, tout en contrôlant les coûts d'exploitation.

Scénario :

1. Situation actuelle :
Tech Innovations Ltd. dispose actuellement d'une infrastructure d'hébergement traditionnelle basée sur des serveurs dédiés. Cependant, ils ont rencontré des problèmes de montée en charge lors d'événements populaires, ce qui a entraîné des temps d'arrêt et une mauvaise expérience utilisateur. De plus, la gestion de l'infrastructure existante est coûteuse en temps et en argent.

2. Besoins du client :
Le client a besoin d'une solution qui peut gérer de manière transparente un afflux massif d'utilisateurs lors de l'événement en direct à venir. Ils souhaitent également réduire les coûts d'exploitation en automatisant la gestion de l'infrastructure autant que possible. Le client est également soucieux de garantir la sécurité de leur service, notamment en ce qui concerne la protection contre les attaques DDoS.

3. Solution proposée :
Le consultant en cloud computing de notre entreprise propose une solution serverless basée sur les services cloud, en mettant en avant les avantages suivants :
   
   a. Évolutivité automatique : Utilisation de services serverless tels que AWS Lambda et Azure Functions pour gérer automatiquement la montée en charge en fonction de la demande, garantissant ainsi que le service reste disponible même en cas d'afflux massif d'utilisateurs.
   b. Gestion automatisée : Utilisation d'outils de gestion de l'infrastructure en tant que code (comme Terraform) pour automatiser la création, la mise à jour et la suppression des ressources cloud, réduisant ainsi la charge de travail de gestion.
   c. Sécurité renforcée : Mise en place de services de sécurité cloud tels que AWS WAF (Web Application Firewall) et Azure DDoS Protection pour protéger contre les menaces en ligne, y compris les attaques DDoS.
   d. Surveillance proactive : Configuration de métriques et d'alertes personnalisées pour surveiller en temps réel les performances du service et être averti en cas de problème.


4. Avantages pour le client :
Tech Innovations Ltd. bénéficiera de cette solution en termes de :
   - Disponibilité continue lors de l'événement en direct, garantissant une 		expérience utilisateur optimale.
   - Réduction significative des coûts d'exploitation grâce à l'automatisation.
   - Sécurité renforcée contre les menaces en ligne.
   - Visibilité améliorée sur la performance du service.

5. Plan de mise en œuvre :
   - Évaluation des besoins spécifiques pour déterminer les services cloud appropriés.
   - Développement d'une architecture serverless.
   - Migration progressive vers la nouvelle infrastructure.
   - Configuration de la surveillance et des alertes.
   - Formation du personnel sur l'utilisation de la nouvelle infrastructure.

En suivant cette approche, Tech Innovations Ltd. sera en mesure de gérer efficacement l'afflux massif d'utilisateurs tout en optimisant les coûts et en garantissant la maintenabilité de leur solution grâce à l'utilisation de services serverless et de cloud computing.








SOLUTION

Dans un premier temps, il serait intéressant de retranscrire les grandes étapes que nous devrons gérer pour répondre à la demande du client.

Analyse du besoin client :
Comprendre en détail les besoins spécifiques du client, y compris les exigences de performance, de sécurité et de scalabilité.

Sélection des services Azure : 
Choisir Azure Functions pour les éléments de calcul serverless.

Conception de l’architecture :
Concevoir une architecture basée sur Azure Functions pour les tâches serverless, telles que le traitement de requêtes API, les tâches de fond, etc.

Développement des fonctions Azure : 
Développer les fonctions Azure nécessaires pour gérer les fonctionnalités de l’application. Nous utiliserons pour cela le Language nodeJS, ce dernier est supporté par Azure.

Base de donnée :
Gérer la base de données avec Azure Cosmos DB en choisissant le modèle de données approprié.

Configuration de la scalabilité automatique : 
Configurer la scalabilité automatique pour les Azure Functions en fonction de la demande. Nous garantirons du coup la gestion d’afflux massif d’utilisateurs.

Tests et validation : 
Effectuer des tests approfondis, y compris des tests de montée en charge, pour nous assurer que l'application fonctionne correctement et peut gérer la charge attendue.

Suivi et optimisation : 
Une fois l'application en production, surveiller en permanence les performances, les coûts et les problèmes de sécurité. Optimiser l'infrastructure au besoin.
Si le client à déjà une infrastructure en place, nous assurons la migration progressive des fonctionnalités vers Azure Functions et Azure


FONCTION
Création du groupe de ressource :
Ce groupe de ressource nous permettra d’accueillir, comme son nom l’indique, de la ressource tel qu’une machine virtuelle, une application de fonction, etc.

<img width="482" alt="image" src="https://github.com/faycalzaazoua/azureDoc/assets/83638729/063fcf9f-dc77-4360-a224-ba847a40606e">


Création d’une application de fonction :

Cette application de fonction va nous permettre de créer des fonctions afin de le injecter du code à tester par la suite.
Le groupe de fonction doit être spécifié par un langage (python, nodeJS, etc.), dans notre cas nous utiliserons une application de fonction en python.
Créer une fonction :
Création de la fonction dans laquelle nous allons déposer notre code python pour ajouter un champ en base de donnée. (CRUD)

Dépôt du code dans la fonction :
Création du groupe base de données :
Création de Service de base de données entièrement managé destiné aux applications pour MongoDB. Puis on récupère la clé de connexion principal afin de l’utiliser dans le code python dans notre fonction crée précédemment.

Par la suite on créer la BDD : 
On lui donne un nom et un id de collection.
Liaison de la BDD avec le code :
On insère dans le morceau de code CREATE le nom de la bdd et collection e également la clé de connexion principale.

Test :
Par la suite nous pouvons essayez d’ajouter un champ en base afin de vérifier que les données saisi seront bien stockés
