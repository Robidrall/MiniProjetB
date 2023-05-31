import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy import linalg
from scipy import signal as sig

#CONSTANTES
F0 = 0.25 
K = 98.8 #diffusivité

#INTERFACE UTILISATEUR
'''dim_x = input("Entrez la dimension x de la plaque")
dim_y = input("Entrez la dimension y de la plaque")
temp_init = input("Entrez la température initiale: ")  
temp_cond_isotherme = input("Entrez la température de condition isotherme en bout de plaque: ")  
x_c = input("Entrez la position x_c du point chaud: ")
y_c = input("Entrez la position y_c du point chaud: ")
n_x = input("Entrez le nombre de point dans la direction x: ")
n_y = input("Entrez le nombre de point dans la direction y: ")
diffusivite = input("Entrez le diffusivité du matériau: ")
amplitude_point_chaud = input()
ecart_type_point_chaud = input()
'''



def Creation_grille(n_x,n_y,taille_x, taille_y):
    X = np.linspace (0,taille_x,n_x+1)
    Y = np.linspace (0,taille_y,n_y+1)
    X,Y = np.meshgrid(X,Y)
    return X,Y 

def Solution_initiale (n_x,n_y,taille_x, taille_y,ecart_type_point_chaud,amplitude_point_chaud) : 
    X,Y = Creation_grille(n_x,n_y,taille_x, taille_y)
    T=amplitude_point_chaud*np.exp(-(((X-x_c)**2/2*ecart_type_point_chaud**2)+((Y-y_c)**2/2*ecart_type_point_chaud**2)))
    plt.contourf(X,Y,T)
    plt.show()
       

    
#Paramètre 
dim_x = 100
dim_y = dim_x 
temp_init = 273
temp_cond_isotherme = 273
x_c = 50
y_c = 50
n_x = 100
n_y = n_x
diffusivite = K
amplitude_point_chaud = 1400
ecart_type_point_chaud = 0.90

Solution_initiale(n_x,n_y,dim_x,dim_y,ecart_type_point_chaud,amplitude_point_chaud) 
