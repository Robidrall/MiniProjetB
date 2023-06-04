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
    n = input(int("Entrez le nombre de segments voulu pour la précision: "))
    return a, b, p1, p2, p3, p4, n

def integration_exacte (a,b,p1,p2,p3,p4):
    I_exacte = p1*(b-a)+p2*(b**2-a**2)/2 +p3*(b**3-a**3)/3 + p4*(b**4-a**4)/4
    return I_exacte
       
def fonction(x,p1,p2,p3,p4):
    return p1 + p2*x +p3*x**2 + p4*x**3

def erreur_integration_num (valeur_exacte, valeur_calcule):
    erreur = abs(valeur_exacte-valeur_calcule)
    return erreur

def Convergence_selon_n (n,a,b,p1,p2,p3,p4,type):
    if type == 'base' : 
        return round(100*erreur_integration_num(integration_exacte(-2,3,p1,p2,p3,p4),methode_des_rectangles_basique(n,a,b,p1,p2,p3,p4))/integration_exacte (a,b,p1,p2,p3,p4),5)
    elif type == 'numpy' : 
        return round(100*erreur_integration_num(integration_exacte(-2,3,p1,p2,p3,p4),methode_des_rectangles_numpy(n,a,b,p1,p2,p3,p4))/integration_exacte (-2,3,p1,p2,p3,p4),5)
    else : 
        print("Le type saisi doit être 'base' ou 'numpy'")
    
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

    plt.plot(np.linspace(15, 100, 85), Tab_I_calcul_numpy[14:99], color='green',label='Intégrale calculée avec la méthode des rectangles numpy')
    plt.plot(np.linspace(15, 100, 75), np.ones(75) * I_exacte, color='blue', label='Intégrale exacte')
    plt.xlabel('Nombre de segment sur l\'intervalle d\'intégration')
    plt.ylabel('Valeur de l\'intégrale')
    plt.title('Valeur de l\'intégrale de la fonction en fonction du nombre de segments en utilisant la méthode des rectangles centrés (numpy)')
    plt.legend()
    plt.grid()
    plt.show()
def tracer_erreur_num_segments(n_max, a, b, p1, p2, p3, p4):
    erreurs_base = []
    erreurs_numpy = []
    n_liste = range(1, n_max + 1)

    for n in n_liste:
        erreur_numpy, erreur_base = Erreur_integration_type(n, a, b, p1, p2, p3, p4)
        erreurs_base.append(erreur_base)
        erreurs_numpy.append(erreur_numpy)

    plt.plot(n_liste, erreurs_base, label='Base')
    plt.plot(n_liste, erreurs_numpy, label='Numpy')
    plt.xlabel('Nombre de segments (n)')
    plt.ylabel('Erreur d\'intégration')
    plt.title('Erreur d\'intégration en fonction du nombre de segments')
    plt.legend()
    plt.grid()
    plt.show()

#print(Convergence_selon_n(15,p1,p2,p3,p4))
#print(Convergence_selon_n(50,p1,p2,p3,p4))
#print(Convergence_selon_n(500,p1,p2,p3,p4))
#print(timeit('Convergence_selon_n(500,p1,p2,p3,p4)',globals=globals(),number=1))







