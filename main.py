# NACA 4 Digit plot program
import numpy as np
import matplotlib.pyplot as plt

# Initialisation des variables
profil = ""
chord = ""
points = ""
distribution = 0
thickness = 0

# Saisi utilisateur des caractéristiques du profil NACA

# Blindage pour s'assurer que l'utilisateur rentre 4 chiffres entiers positifs
while len(profil) != 4 or profil.isnumeric() == False:
    profil = str(input("Veillez choisir un profil NACA 4 chiffres : "))

thickness = float(profil[2:]) / 100
# Convertit la chaine de caractere en deux chiffres flottants et met en %
# Recupere les 2 derniers chiffres saisis par l'utilisateur

print(f"Epaisseur du profil = {thickness * 100}%")

while not chord.isnumeric(): # Blindage pour s'assurer que l'utilisateur ne rentre que des entiers positifs
    chord = str(input("Veillez choisir la taille de la corde en mètre : "))  # Taille de la corde
chord = float(chord[::]) # On convertit la chaine de caractère saisie en nombre réel

while not points.isnumeric(): # Même blindage pour n'avoir que des entiers positifs saisis
    points = input('Combien de points souhaitez vous pour tracer le graphique ?'
                   '\nVeillez choisir un nombre entier\n ')
points = int(points[::]) # On convertit la chaîne saisie en nombre entier

# Permet de choisir quelle distribution souhaite l'utilisateur, linéaire ou non uniforme
# Blindage pour que l'utilisateur ne puisse saisir que 1 ou 2
while distribution != 1 and distribution != 2:
    distribution = int(input("Pour finir, souhaitez vous une distribution de point linéaire ou"
                             "non uniforme ? \n1 : Linéaire \n2 : Non uniforme\n"
                             "Tapez 1 ou 2\n"))

###### Creation des arrays pour les tableaux de coordonnées du profil choisi par l'utilisateur

# On crée un array allant de 0 à 1 avec un nombre de points choisi par l'utilisateur
xc_linear = np.linspace(0, 1, points)

# On fait la même chose pour la distribution non uniforme de 0 à pi
teta = np.linspace(0, np.pi, points)
xc_non_uniform = 0.5 * (1 - np.cos(teta))

#### Calcul des demis-épaisseurs du profil avec les tableaux remplis précedemments
yt_linear = 5 * thickness * (0.2969 * np.sqrt(xc_linear) - 0.1260 * xc_linear - 0.3516 * xc_linear ** 2
                             + 0.2843 * xc_linear ** 3 - 0.1036 * xc_linear ** 4)

yt_non_uniform = 5 * thickness * (
        0.2969 * np.sqrt(xc_non_uniform) - 0.1260 * xc_non_uniform - 0.3516 * xc_non_uniform ** 2
        + 0.2843 * xc_non_uniform ** 3 - 0.1036 * xc_non_uniform ** 4)

# Création des courbes du profil
x_up_linear = xc_linear * chord
x_down_linear = xc_linear * chord
y_up_linear = yt_linear * chord
y_down_linear = -yt_linear * chord

x_up_non_uniform = xc_non_uniform * chord
x_down_non_uniform = xc_non_uniform * chord
y_up_non_uniform = yt_non_uniform * chord
y_down_non_uniform = -yt_non_uniform * chord

###### EPAISSEUR MAXIMUM ########
thickness_max_position_linear = np.argmax(y_up_linear)
thickness_max_position_non_uniform = np.argmax(y_up_non_uniform)

print(f"La position de l'épaisseur maximale le long de la corde se situe à "
      f"\n{x_up_linear[thickness_max_position_linear]} mètres pour une distribution linéaire," 
      f"\n{x_up_non_uniform[thickness_max_position_non_uniform]} mètres pour une distribution non uniforme")

print(f"\nLa valeur de l'épaisseur maximale est : "
      f"\nLinéaire_max = {y_up_linear[thickness_max_position_linear] * 2} mètres"
      f"\nNon_uniforme_max = {y_up_non_uniform[thickness_max_position_non_uniform] * 2} mètres")

if distribution == 1:
    print("\nVous avez choisi une distribution linéaire\n")
    plt.axis('equal')
    plt.plot(x_up_linear, y_up_linear, label='intrados')
    plt.plot(x_down_linear, y_down_linear, label='extrados')
    plt.scatter(x_up_linear[thickness_max_position_linear], y_up_linear[thickness_max_position_linear],
                label='épaisseur maximale', color='green')
    plt.scatter(x_up_linear[thickness_max_position_linear], -y_up_linear[thickness_max_position_linear],
                color='green')
    plt.xlabel('axe x')
    plt.ylabel('axe y')
    plt.legend()
    plt.grid()
    plt.title(f'Profil NACA{profil} distribution linéaire')
    plt.show()

elif distribution == 2:
    print("\nVous avez choisi une distribution non uniforme\n")
    plt.axis('equal')
    plt.plot(x_up_non_uniform, y_up_non_uniform, label='intrados')
    plt.plot(x_down_non_uniform, y_down_non_uniform, label='extrados')
    plt.scatter(x_up_non_uniform[thickness_max_position_non_uniform], y_up_non_uniform[thickness_max_position_non_uniform],
                label='épaisseur maximale', color='green')
    plt.scatter(x_up_non_uniform[thickness_max_position_non_uniform], -y_up_non_uniform[thickness_max_position_non_uniform],
                color='green')
    plt.xlabel('axe x')
    plt.ylabel('axe y')
    plt.legend()
    plt.grid()
    plt.title(f'Profil NACA{profil} distribution non uniforme')
    plt.show()

else:
    print("ce cas n'est pas prit en compte")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
