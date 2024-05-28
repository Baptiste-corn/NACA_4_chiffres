# NACA 4 Digit plot program
import numpy as np
import matplotlib.pyplot as plt


profil = str(input ("Veillez choisir votre profil NACA 4 chiffres : "))
thickness = float(profil[2 :]) / 100  # Epaisseur de la corde en %
print(thickness)

chord = int(input("Veillez choisir la taille de la corde en metre : "))
points = int(input("Combien de points en abscisse souhaitez vous pour tracer le graphique ?"
                             "\nVeillez choisir un nombre entier\n "))

distribution = int(input("Pour finir, souhaitez vous une destribution de point linéaire ou"
                     "non uniforme ? \n1 : Lineaire \n2 : Non uniforme\n"
                     "Tapez 1 ou 2\n"))

xc_linear = np.linspace(0, 1, points)

teta = np.linspace(0, np.pi, points)
xc_non_uniform = 0.5 * (1 - np.cos(teta))

yt_linear = 5*thickness * (0.2969*np.sqrt(xc_linear) - 0.1260*xc_linear - 0.3516*xc_linear**2
                            + 0.2843*xc_linear**3 - 0.1036*xc_linear**4)

yt_non_uniform = 5*thickness * (0.2969*np.sqrt(xc_non_uniform) - 0.1260*xc_non_uniform - 0.3516*xc_non_uniform**2
                            + 0.2843*xc_non_uniform**3 - 0.1036*xc_non_uniform**4)

x_up_linear = xc_linear*chord
x_down_linear = xc_linear*chord
y_up_linear = yt_linear*chord
y_down_linear = -yt_linear*chord

x_up_non_uniform = xc_non_uniform*chord
x_down_non_uniform = xc_non_uniform*chord
y_up_non_uniform = yt_non_uniform*chord
y_down_non_uniform = -yt_non_uniform*chord


###### EPAISSEUR MAXIMUM ########
thickness_max_position_linear = np.argmax(y_up_linear)
thickness_max_position_non_uniform = np.argmax(y_up_non_uniform)
print(f"Voici la position de l'épaisseur maximale le long de la corde"
      f"\nDistribution linéaire  : {x_up_linear[thickness_max_position_linear]}, "
      f"\nDistribution non uniforme : {x_up_non_uniform[thickness_max_position_non_uniform]}")
print(f"La valeur de l'épaisseur maximale est : "
      f"\nLinéaire_max = {y_up_linear[thickness_max_position_linear] * 2} mètres"
      f"\nNon_uniforme_max = {y_up_non_uniform[thickness_max_position_non_uniform] * 2} mètres")

if distribution == 1:
    print("\nVous avez choisi une distribution linéaire\n")
    plt.axis('equal')
    plt.plot(x_up_linear, y_up_linear)
    plt.plot(x_down_linear, y_down_linear)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.title(f'Profil NACA{profil} distribution linéaire')
    plt.show()

elif distribution == 2:
    print("\nVous avez choisi une distribution non uniforme\n")
    plt.axis('equal')
    plt.plot(x_up_non_uniform, y_up_non_uniform)
    plt.plot(x_down_non_uniform, y_down_non_uniform)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.title(f'Profil NACA{profil} distribution non uniforme')
    plt.show()

else:
    print("ce cas n'est pas prit en compte")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
