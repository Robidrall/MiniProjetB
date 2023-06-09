'''
Mini Projet B - Equation de la Chaleur
MGA802 
CHAMBAZ-ROBILLARD
'''

import numpy as np
import matplotlib.pyplot as plt


#CONSTANTES
F0 = 0.25
diffusivite = 5

#INTERFACE UTILISATEUR
def créer_arguments():
    entree = input("Voulez vous définir vos propres coefficients (oui ou non)?\nDans le cas contraires des coefficients de base seront affectés : ")
    if entree == 'oui':
        dim_x = int(input("Entrez la dimension x de la plaque : "))
        dim_y = int(input("Entrez la dimension y de la plaque : "))
        temp_init = int(input("Entrez la température initiale: "))
        temp_cond_isotherme = int(input("Entrez la température de condition isotherme en bout de plaque: "))
        x_c = int(input("Entrez la position x_c du point chaud: "))
        y_c = int(input("Entrez la position y_c du point chaud: "))
        n_x = int(input("Entrez le nombre de point dans la direction x: "))
        n_y = int(input("Entrez le nombre de point dans la direction y: "))
        amplitude_point_chaud = int(input("Entrez l'amplitude du point chaud: "))
        ecart_type_point_chaud = float(input("Entrez l'écart-type lié au point chaud: "))
        ITERATION = int(input("Entrez le nombre d'itérations désiré: "))
    elif entree =='non':
        dim_x = 20
        dim_y = dim_x
        temp_init = 25
        temp_cond_isotherme = 25
        x_c = 4
        y_c = 7
        n_x = 100
        n_y = n_x
        ITERATION = 100
        amplitude_point_chaud = 90
        ecart_type_point_chaud = 0.9
    return dim_x, dim_y, temp_init, temp_cond_isotherme, x_c, y_c, n_x, n_y, amplitude_point_chaud, ecart_type_point_chaud, ITERATION

dim_x, dim_y, temp_init, temp_cond_isotherme, x_c, y_c, n_x, n_y, amplitude_point_chaud, ecart_type_point_chaud, ITERATION = créer_arguments()
delta_x = dim_x / n_x
delta_y = dim_y / n_y

def Calcul_T(x0,y0,X,Y) : 
    '''
    Cette fonction renvoi une matrice contenant la température en chaque point 
    '''
    return amplitude_point_chaud*np.exp(-(((X-x0)**2/2*ecart_type_point_chaud**2)+((Y-y0)**2/2*ecart_type_point_chaud**2)))

def Creation_grille():
    '''
    Cette fonction créé la grille 
    '''
    X = np.linspace (0,dim_x,n_x+1)
    Y = np.linspace (0,dim_y,n_y+1)
    X,Y = np.meshgrid(X,Y)
    return X,Y 

def Application_Condition_Limite(T,temp_cond_isotherme):
    '''
    Permet d'appliquer les conditions aux limites en fixant une valeur (temperature condition isotherme) 
    à la limite de notre matrice de température
    '''
    T[:,-1] = temp_cond_isotherme
    T[:,0] = temp_cond_isotherme
    T[0,:] = temp_cond_isotherme
    T[-1,:] = temp_cond_isotherme
    return T

def Solution_initiale (X,Y) : 
    '''
    Cette fonction permet d'initialiser le modèle et de l'afficher
    '''
    T_init=Calcul_T(x_c,y_c,X,Y)+temp_init
    T_init=Application_Condition_Limite(T_init,temp_cond_isotherme)
    plt.contourf(X,Y,T_init)
    plt.colorbar()
    plt.show()
    return T_init
        
def Visualisation_temperature_instantanee (T): 
    '''
    Cette fonction permet de visualiser la température à un instant t sur un graphique
    '''
    X,Y = Creation_grille()
    plt.contourf(X,Y,T)
    plt.colorbar()
    plt.show()

def Calcul_RHS(T,diffusivite):
    '''
    Cette fonction retourne une matrice correspondant au RHS nécessaire pour évaluer la propagation de la chaleur
    '''
    #On effectue les calculs sur des matrices plus petites puis on la copie ensuite au centre d'une matrice de zeros
    #On obtient ainsi une matrice avec des zéros à l'extérieur (ce qui est nécessaire pour les conditions limites)
    RHS_petite = diffusivite*(((T[2:,1:-1]-2*T[1:-1,1:-1]+T[:-2,1:-1])/(dim_x / n_x)**2)+((T[1:-1,:-2]-2*T[1:-1,1:-1]+T[1:-1,2:])/(dim_y / n_y)**2))
    RHS_grande = np.zeros((RHS_petite.shape[0]+2,RHS_petite.shape[1] + 2))
    RHS_grande[1:-1,1:-1] = RHS_petite
    return RHS_grande

def Avancement_temporel (T,diffusivite,dt): 
    '''
    Cette fonction réalise l'avancement temporel et permet de passer de t à t+1
    '''
    #Calcul de T(t+1)
    T_Suivant = T+dt*Calcul_RHS(T,diffusivite)
    #Application des conditions aux limites
    T_Suivant = Application_Condition_Limite(T_Suivant,temp_cond_isotherme) 
    return T_Suivant    
    
def Calcul_Résidu(T_Precedent,T_Actuel):
    '''
    Cette fonction retourne le résidu permettant de calculer les normes et d'étudier 
    la convergence du champs de température
    '''
    return (T_Actuel - T_Precedent)/T_Actuel
    


def calcul_temp(T_init, diffusivite, dt):
    #Initialisation des tableaux de températures et de normes pour le tracé des courbes    
    Temperature_max = np.array(np.amax(T_init))
    Temperature_min = np.array(np.amin(T_init))
    Temperature_moy = np.array(np.mean(T_init))
    Norme_L2 = np.array(0)
    Norme_Infini = np.array(0)
    
    #On boucle pour similuer permettre d'avancer dans le temps et de voir la propagation 
    for t in range(1,ITERATION): 
        #On réalise l'avancement temporel
        T_suivant = Avancement_temporel(T_init,diffusivite,dt)
        #On affiche le graphe a intervalle de temps régulier (10 fois) 
        if t%(ITERATION/10) == 0 :
            Visualisation_temperature_instantanee(T_suivant)
        
        #Calcul du résidu et stockage de la norme L2 et Linfini     
        Residu = Calcul_Résidu(T_init,T_suivant) 
        Norme_L2 = np.append(Norme_L2,np.linalg.norm(Residu))
        Norme_Infini = np.append(Norme_Infini, np.amax(np.abs(Residu)) )
                
        #Stockage des températures min, max et moyenne 
        Temperature_max=np.append(Temperature_max, [np.amax(T_suivant)])
        Temperature_min=np.append(Temperature_min, [np.amin(T_suivant)])
        Temperature_moy=np.append(Temperature_moy, [np.mean(T_suivant)])
        
        #La nouvelle valeur devient la valeur initiale pour la prochaine itération
        T_init=T_suivant
    return Temperature_max, Temperature_min, Temperature_moy, Norme_Infini, Norme_L2

def tracer_temperature(Tmax, Tmin, Tmoy):
    #Affichage du graphique de l'évolution des températures minimale, maximale et moyenne en fonction du temps
    plt.plot(np.linspace(0, ITERATION, ITERATION), Tmax, color='red', label='Temperature maximale')
    plt.plot(np.linspace(0, ITERATION, ITERATION), Tmin, color='blue', label='Temperature minimale')
    plt.plot(np.linspace(0, ITERATION, ITERATION), Tmoy, color='green', label='Temperature moyenne')
    plt.xlabel('Temps (s)')
    plt.ylabel('Température')
    plt.title('Valeur de la température en fonction du temps')
    plt.legend()
    plt.grid()
    plt.show()

def tracer_norme(L2,Inf):
    #Affichage du graphique de l'évolution des normes L2 et Linfini
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    axs[0].plot(np.linspace(1,ITERATION, ITERATION-1), L2[1:], color='red', label='Norme L2')
    axs[0].set_xlabel('Temps')
    axs[0].set_ylabel('Norme L2')    
    axs[1].plot(np.linspace(1,ITERATION, ITERATION-1), Inf[1:], color='blue', label='Norme Linfini')
    axs[1].set_xlabel('Temps')
    axs[1].set_ylabel('Norme Linfini')
    plt.title('Valeur des normes L2 et Linfini pour étudier la convergence du champs de température', loc='right')
    plt.grid()
    plt.show()






