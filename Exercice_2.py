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
    return T_init
       
def Visualisation_temperature_instantanee (T): 
    X,Y = Creation_grille()
    plt.contourf(X,Y,T)
    plt.colorbar()
    plt.show()

def Calcul_RHS(T,diffusivite):
    RHS_petite = diffusivite*(((T[2:,1:-1]-2*T[1:-1,1:-1]+T[:-2,1:-1])/delta_x**2)+((T[1:-1,:-2]-2*T[1:-1,1:-1]+T[1:-1,2:])/delta_y**2))
    
    RHS_grande = np.ones((RHS_petite.shape[0]+2,RHS_petite.shape[1] + 2))*temp_cond_isotherme
    RHS_grande[1:-1,1:-1] = RHS_petite
    return RHS_grande

def Avancement_temporel (T,diffusivite): 
    dt = (F0*delta_x**2)/K
    T_Suivant = T+dt*Calcul_RHS(T,diffusivite)
    return T_Suivant    
    

    
def Main() : 
    #Création de la grille 
    print("Création de la grille")
    X,Y=Creation_grille()
    #Affichage des conditions initiales
    print("Affichage des conditions initiales")     
    T_init = Solution_initiale(X,Y)
    #Avancement temporel 
    
    for t in range(1,100): 
        T_Suivant = Avancement_temporel(T_init,diffusivite)
        T_init=T_Suivant
        if t%2 == 0 :
            Visualisation_temperature_instantanee(T_Suivant)
            
        

    
    
    
       
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
