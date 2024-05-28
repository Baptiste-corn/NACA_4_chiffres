# NACA 4 Digit plot program
import numpy as np
import matplotlib.pyplot as plt


profil = str(input ("Veillez choisir votre profil NACA 4 chiffres : "))
thickness = int(profil[2 :]) / 100  # Epaisseur de la corde en %

chord = int(input("Veillez choisir la taille de la corde en metre : "))
points = int(input("Combien de points en abscisse souhaitez vous pour tracer le graphique ?"
                             "\nVeillez choisir un nombre entier\n "))

distribution = input("Pour finir, souhaitez vous une destribution de point linéaire ou"
                     "non uniforme ? \n1 : Lineaire \n2 : Non uniforme\n"
                     "Tapez 1 ou 2")

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


plt.axis('equal')
plt.plot(x_up_linear, y_up_linear)
plt.plot(x_down_linear, y_down_linear)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title(f'Profil NACA{profil}')
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
