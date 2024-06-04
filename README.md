# Ce programme a pour objectif de représenter graphiquement un profil d'aile NACA 4 chiffres symétrique. 

# L'utilisateur doit rentrer plusieurs données : 
- Les 4 chiffres du profil NACA pour obtenir ses caractéristiques comme l'épaisseur maximale
- La longueur de la corde de l'aile en mètre
- le nombre de points nécessaires pour tracer le graphique, plus il y a de points, plus le tracé sera précis cependant le temps de compilation sera plus long
- le type de distribution de points, linéaire ou non uniforme

  # Stratégie de développement
  Le code comprend plusieurs parties :
  - La saisie des données par l'utilisateur, avec blindage de code pour qu'il ne puisse saisir que le format de données demandé (ex: saisir uniquement des entiers positifs, pas de lettre)
  - le calcul des demi-épaisseurs du profil selon les données rentrées par l'utilisateur. Chaque demi-épaisseur est calculée selon une répartion linéaire ou non uniforme.
Le calcul est réalisé à l'aide de la librairie numpy
  - L'affichage des calculs à l'aide la librairie matplotlib. On affiche le profil d'aile basé sur les données saisies par l'utilisateur.
On affiche également où se situe l'épaisseur maximum du profil, que l'on a préalablement calculée.

# Références utilisées : 
Librairies numpy et matplotlib
Stack Overflow
