# projet_GeekOfLegends

GeekOfLegends
 

Configuration du Projet
 

Créez un repository Github. en PRIVATE
Utilisez une structure de dossier organisée.
Commitez avec des noms explicites.
 

Création des Boss
 
Créez trois boss : Sauron, Chronos, Lilith.
Chaque boss a un nom, des points de vie et d'attaque.
Énigmes pour les Boss

Quand un boss a 20% de points de vie, posez une énigme.
Choisissez aléatoirement parmi au moins 3 énigmes.
 

Création des Héros
Créez un guerrier, un mage, et un archer.
Chaque héros a un nom, des points de vie et d'attaque.

Actions du Guerrier

Guerrier : Défense et Attaque.
Gagne 1 point de rage par tour.
À 4 points de rage, gagne 25% d'attaque pendant 1 tour.
Actions du Mage

Mage : Défense et Attaque.
Les attaques coûtent 2 points de mana.
Récupère 7 points de mana s'il n'a plus assez.
 Actions de l'Archer

Archer : Défense et Attaque.
Les attaques consomment 2 flèches.
Récupère 6 flèches s'il n'en a plus.

Postures des Héros

Choisissez une posture pour chaque héros : Défense ou Attaque.
 

Combat
Chaque tour, les trois héros attaquent le boss.
Le boss attaque aléatoirement un des héros.
a chaque tour une des posture est choisie
 
 Enigmes et Réponses

Si le boss a 20% de points de vie, posez une énigme.
L'utilisateur a 3 essais pour répondre correctement.
 
 Résolution des Énigmes

Transformez les réponses en minuscules et supprimez les espaces.
Vérifiez si la bonne réponse est contenue dans la réponse de l'utilisateur.
 
Choix Aléatoire du Boss

Choisissez aléatoirement un boss parmi les trois.
 
Attaques et Défenses

Définissez les effets des attaques et défenses.
l'attaque fais 1.4 fois plus de degat et la defense divise par deux l'attaque du boss
 

Interactions Utilisateur
Laissez l'utilisateur choisir le nom des héros.
Fixez un total de points de vie et d'attaque à distribuer entre les héros.

Gestion des Points de Vie et d'Attaque

Distribuez les points de vie et d'attaque entre les héros selon les choix de l'utilisateur.
 

________________________________________________________________________________________________________________

 

BONUS
 

Gestion du Cimetière

Si un héros meurt, poussez-le dans un cimetière.
 
 Énigme "Python"

Ajoutez une énigme liée à Python.

Effets Visuels dans le terminal

Améliorez les messages dans la terminal pour raconter l'histoire de manière dynamique.
Ces étapes devraient vous guider pour créer un jeu interactif et engageant en utilisant Python.

 

BON COURAGE ! 

Rajout d'un attribut pour le héros : argent
__shop :__ création de shop qui permettra à un héros d'acheter une arme (si l argent suffit). 
Option 1) voir tout le panier.
Option 2) acheter.
Option 3) vendre (-15% sur l'achat de base + un random (0-60)). ex : 100 - 15% - random -> 33% = 100 - 48% = 52 à la vente.
Ce random se fait après chaque round (on en parle apres)
Option 4) exit.
comprendre qu'il y a des types d'armes càd une arme par type de héros.
Le heros ne peut pas posséder plusieurs arme (sauf si vous rajouter un heors qui a cette capacité.) et doit s’équiper de celle qu'il achète.. se déséquiper de l'ancienne.

__Forgeron :__ Creation d'une forge où le forgeron -> pourra ameliore votre arme si vous le payez et si vous avez l'equipement necessaire
Option 1)  