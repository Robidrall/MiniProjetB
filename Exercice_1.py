import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit
import time

def créer_arguments():
    a = input(int("Entrez la borne inférieur de l'intervalle: "))
    b = input(int("Entrez la borne supérieure de l'intervalle: "))
    p1 = input(int("Entrez le coefficient p1 du polynôme: "))
    p2 = input(int("Entrez le coefficient p2 du polynôme: "))
    p3 = input(int("Entrez le coefficient p3 du polynôme: "))
    p4 = input(int("Entrez le coefficient p4 du polynôme: "))
    n = input(int("Entrez le nombre de segments voulu pour la précision (nombre positif): "))
    return a, b, p1, p2, p3, p4, n

#Cette fonction représente le calcul de l'intégrale exacte
def integration_exacte (a,b,p1,p2,p3,p4):
    I_exacte = p1*(b-a)+p2*(b**2-a**2)/2 +p3*(b**3-a**3)/3 + p4*(b**4-a**4)/4
    return I_exacte

#Cette fonction permet de représenter la fonction polynomiale d'ordre 3
def fonction(x,p1,p2,p3,p4):
    return p1 + p2*x +p3*x**2 + p4*x**3

# L'erreur est la soustraction de la valeure exacte - la valeur calculée
def erreur_integration_num (valeur_exacte, valeur_calcule):
    erreur = abs(valeur_exacte-valeur_calcule)
    return erreur
    
#Méthode des rectangles utilisant du python de base
def methode_des_rectangles_basique(n,a,b,p1,p2,p3,p4):
   I_calc = 0
   pas = (b - a) / n
   intervalle = [a + i * pas for i in range(n + 1)]
   for i in range(n):
        aire = fonction(intervalle[i] + (intervalle[i + 1] - intervalle[i])/2, p1, p2, p3, p4) * (intervalle[i + 1] - intervalle[i])
        I_calc += aire
   return I_calc

#Méthode des rectangles en utilisant la librairie NUMPY
def methode_des_rectangles_numpy(n,a,b,p1,p2,p3,p4): 
    abscisse_bord_rectangle = np.linspace(a,b,n+1)
    abscisse_centre_rectangle = abscisse_bord_rectangle[:-1] + ((b-a)/(2*n))
    ordonnee_centre_rectangle = fonction(abscisse_centre_rectangle,p1,p2,p3,p4)
    aire_totale = np.sum(ordonnee_centre_rectangle*(b-a)/n)
    return aire_totale

#Cette fonction permet de définir la convergence en fonction du nombre de segments pour chaque méthode
def Convergence_selon_n (n,a,b,p1,p2,p3,p4,type):
    if type == 'base' :
        convergence_base = round(100*erreur_integration_num(integration_exacte(a,b,p1,p2,p3,p4),methode_des_rectangles_basique(n,a,b,p1,p2,p3,p4))/integration_exacte (a,b,p1,p2,p3,p4),5)
        return convergence_base
    elif type == 'numpy' :
        convergence_numpy = round(100*erreur_integration_num(integration_exacte(a,b,p1,p2,p3,p4),methode_des_rectangles_numpy(n,a,b,p1,p2,p3,p4))/integration_exacte (a,b,p1,p2,p3,p4),5)
        return convergence_numpy
    else :
        print("Le type saisi doit être 'base' ou 'numpy'")

def Erreur_integration_type(n,a,b,p1,p2,p3,p4):
        I_calcul_base = methode_des_rectangles_basique(n, a, b, p1, p2, p3, p4)
        I_exacte = integration_exacte(a, b, p1, p2, p3, p4)
        erreur_integration_base = erreur_integration_num(I_exacte, I_calcul_base)

        I_calcul_numpy = methode_des_rectangles_numpy(n, a, b, p1, p2, p3, p4)
        I_exacte = integration_exacte(a, b, p1, p2, p3, p4)
        erreur_integration_numpy = erreur_integration_num(I_exacte, I_calcul_numpy)

        return erreur_integration_numpy, erreur_integration_base

def tracer_convergence(n_max, a, b, p1, p2, p3, p4):
    convergences = []
    n_liste = range(1, n_max + 1)

    for n in n_liste:
        I_exacte = integration_exacte(a, b, p1, p2, p3, p4)
        I_rectangles = methode_des_rectangles_basique(n, a, b, p1, p2, p3, p4)
        convergence = I_exacte - I_rectangles
        convergences.append(convergence)

    plt.plot(n_liste, convergences)
    plt.xlabel('Nombre de segments (n)')
    plt.ylabel('Convergence (Intégrale exacte - Intégrale méthode des rectangles)')
    plt.title('Convergence de l\'intégrale en fonction du nombre de segments')
    plt.grid()
    plt.show()

def tracer_Integrales_segment(I_exacte,n, a, b, p1, p2, p3, p4):
    # Affichage des courbes et des valeurs de convergences à n = 15, 100 et 500

    Tab_I_calcul_base = np.zeros((500))
    Tab_I_calcul_numpy = np.zeros((500))
    for n in range(1, 501):
        I_calcul_base = round(methode_des_rectangles_basique(n, a, b, p1, p2, p3, p4), 5)
        I_calcul_numpy = round(methode_des_rectangles_numpy(n, a, b, p1, p2, p3, p4), 5)
        Tab_I_calcul_base[n - 1] = I_calcul_base
        Tab_I_calcul_numpy[n - 1] = I_calcul_numpy
        if n == 15 or n == 50 or n == 500:
            erreur_integration_numpy = erreur_integration_num(I_exacte, I_calcul_numpy)
            erreur_integration_base = erreur_integration_num(I_exacte, I_calcul_base)
            erreur_integration_prct_numpy = round(erreur_integration_numpy * 100, 5)
            print(f"L'erreur d'intégration (pour n={n}) est de {erreur_integration_numpy} soit environ {erreur_integration_prct_numpy}%\n")

    '''#Premier plot de 1 à 500 (on voit pas grand chose)    
        plt.plot(np.linspace(1,500,500),Tab_I_calcul,color='red',label='Intégrale calculée avec la méthode des rectangles')
        plt.plot(np.linspace(1,500,500),np.ones(500)*I_exacte,color='blue',label='Intégrale exacte')
        plt.xlabel('Nombre de segment sur l\'intervalle d\'intégration')
        plt.ylabel('Valeur de l\'intégrale')
        plt.legend()
        plt.grid()
        plt.show()'''

    # Second plot de 15 à 100 (On voit la convergence)
    plt.plot(np.linspace(15, 100, 85), Tab_I_calcul_base[14:99], color='red',label='Intégrale calculée avec la méthode des rectangles de base')
    plt.plot(np.linspace(15, 100, 75), np.ones(75) * I_exacte, color='blue', label='Intégrale exacte')
    plt.xlabel('Nombre de segment sur l\'intervalle d\'intégration')
    plt.ylabel('Valeur de l\'intégrale')
    plt.title('Valeur de l\'intégrale de la fonction en fonction du nombre de segments en utilisant la méthode des rectangles centrés (de base)')
    plt.legend()
    plt.grid()
    plt.show()

    #Meme principe pour la méthode avec Numpy qui a la meme précision, nous la laissons en commentaire car le tracé est le meme.
    """plt.plot(np.linspace(15, 100, 85), Tab_I_calcul_numpy[14:99], color='green',label='Intégrale calculée avec la méthode des rectangles numpy')
    plt.plot(np.linspace(15, 100, 75), np.ones(75) * I_exacte, color='blue', label='Intégrale exacte')
    plt.xlabel('Nombre de segment sur l\'intervalle d\'intégration')
    plt.ylabel('Valeur de l\'intégrale')
    plt.title('Valeur de l\'intégrale de la fonction en fonction du nombre de segments en utilisant la méthode des rectangles centrés (numpy)')
    plt.legend()
    plt.grid()
    plt.show()"""

def tracer_temps_execution_segments(n, a, b, p1, p2, p3, p4):
    #On sépare le temps en deux tableaux, un pour la méthode de base et pour numpy
    temps_base = []
    temps_numpy = []
    n_liste = range(1, n + 1)

    for n in n_liste:
        # Mesurer le temps d'exécution pour la méthode avec du python de base
        # La fonction lambda est utilisée pour réaliser l'appel à la méthode des rectangles avec les arguments.
        # Elle créée une fonction anonyme qui représente le code que l'on souhaite mesurer avec le temps d'exécution.
        temps_base.append(timeit(lambda: methode_des_rectangles_basique(n, a, b, p1, p2, p3, p4), number=1))

        # Mesurer le temps d'exécution pour la méthode numpy
        temps_numpy.append(timeit(lambda: methode_des_rectangles_numpy(n, a, b, p1, p2, p3, p4), number=1))

    #Procédure pour tracer le temps d'exécution en fonction de n
    plt.plot(n_liste, temps_base, color='red', label='Base')
    plt.plot(n_liste, temps_numpy, color='green', label='Numpy')
    plt.xlabel('Nombre de segments (n)')
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Temps d'exécution en fonction du nombre de segments")
    plt.legend()
    plt.grid()
    plt.show()

#print(Convergence_selon_n(15,p1,p2,p3,p4))
#print(Convergence_selon_n(50,p1,p2,p3,p4))
#print(Convergence_selon_n(500,p1,p2,p3,p4))
#print(timeit('Convergence_selon_n(500,p1,p2,p3,p4)',globals=globals(),number=1))







