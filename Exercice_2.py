import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy import linalg
from scipy import signal as sig

#CONSTANTES
F0 = 0.25 
K = 98.8 #diffusivité

'''#INTERFACE UTILISATEUR
dim_x = input("Entrez la dimension x de la plaque")
dim_y = input("Entrez la dimension y de la plaque")
temp_init = input("Entrez la température initiale: ")  
temp_cond_isotherme = input("Entrez la température de condition isotherme en bout de plaque: ")  
x_c = input("Entrez la position x_c du point chaud: ")
y_c = input("Entrez la position y_c du point chaud: ")
n_x = input("Entrez le nombre de point dans la direction x: ")
n_y = input("Entrez le nombre de point dans la direction y: ")
diffusivite = input("Entrez le diffusivité du matériau: ")
amplitude_point_chaud = input()
ecart_type_point_chaud = input()'''


def Calcul_T(x0,y0,X,Y) : 
    return amplitude_point_chaud*np.exp(-(((X-x0)**2/2*ecart_type_point_chaud**2)+((Y-y0)**2/2*ecart_type_point_chaud**2)))

def Creation_grille():
    X = np.linspace (0,dim_x,n_x+1)
    Y = np.linspace (0,dim_y,n_y+1)
    X,Y = np.meshgrid(X,Y)
    return X,Y 

def Solution_initiale (X,Y) : 
    T_init=Calcul_T(x_c,y_c,X,Y)
    plt.contourf(X,Y,T_init)
    plt.colorbar()
    plt.show()
       
def Visualisation_temperature_instantanee (T): 
    X,Y = Creation_grille()
    plt.contourf(X,Y,T)
    plt.colorbar()
    plt.show()

def Calcul_RHS(x0,y0,X,Y,diffusivite,x_b,y_b):
    #A voir si on doit appliquer les conditions aux différents termes de terme_1 et terme_2
    if x0 >= x_b or x0 <= 0 or y0 <= 0 or y0 >= y_b :  
        #Prise en compte des conditions limites
        return 0
    else : 
        terme_1 = (Calcul_T(x0+delta_x,y0,X,Y)+Calcul_T(x0-delta_x,y0,X,Y)-2*Calcul_T(x0,y0,X,Y))/(delta_x**2)
        terme_2 = (Calcul_T(x0,y0+delta_y,X,Y)+Calcul_T(x0,y0-delta_y,X,Y)-2*Calcul_T(x0,y0,X,Y))/(delta_y**2)
        return diffusivite*(terme_1+terme_2)

def Avancement_temporel (x0, y0, X, Y): 
    dt = (F0*delta_x**2)/K
    T_suivant=Calcul_T(x_c,y_c,X,Y)
    for i in range(0,dim_x) :
        for j in range(0,dim_y) : 
            # T_suivant[i][j] = T_suivant[i][j] + dt*Calcul_RHS(i,j,X,Y,diffusivite,dim_x,dim_y) bug !!
    Visualisation_temperature_instantanee(T_suivant)

    
def Main() : 
    #Création de la grille 
    print("Création de la grille")
    X,Y=Creation_grille()
    #Affichage des conditions initiales
    print("Affichage des conditions initiales")     
    Solution_initiale(X,Y)
    #Avancement temporel 
    Avancement_temporel(x_c,y_c,X, Y)
    
    
    
    
       
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
delta_x = dim_x/n_x
delta_y = dim_y/n_y

Main()
