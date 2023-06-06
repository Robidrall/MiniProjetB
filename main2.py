'''
Mini Projet B - Équation de la chaleur
MGA802 
CHAMBAZ-ROBILLARD
'''

import Exercice_2 as ex2
import time as time

#CONSTANTES en appelant le module
F0 = ex2.F0
K = ex2.K
ITERATION = ex2.ITERATION

def Main():
    '''
    Cette fonction est la fonction principale du programme, elle synchronise les autres fonctions et affiche les graphes d'analyse
    '''
    # Création de la grille
    print("Création de la grille")
    X, Y = ex2.Creation_grille()
    # Affichage des conditions initiales
    print("Affichage des conditions initiales")
    T_init = ex2.Solution_initiale(X, Y)

    # Calcul du pas temporel
    dt = (F0 * ex2.delta_x ** 2) / K

    Temperature_max, Temperature_min, Temperature_moy, Norme_L2, Norme_Infini = ex2.calcul_temp(T_init, K, dt)

    ex2.tracer_temperature(Temperature_max, Temperature_min, Temperature_moy)

    ex2.tracer_norme(Norme_L2, Norme_Infini)



temps_debut = time.perf_counter()
Main()
temps_fin = time.perf_counter()

print(f"Temps de compilation :{temps_fin - temps_debut} secondes")
