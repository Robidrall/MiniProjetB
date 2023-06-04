#On importe le module Exercice_1 ou toutes les fonctions sont présentes
import Exercice_1 as ex1
from timeit import timeit

#Valeurs de test
p1 = 5
p2 = 2
p3 = 4
p4 = 2
a = -2
b = 3
n = 50

#Interface utilisateur qui choisit ses coefficients
#a, b, p1, p2, p3, p4 = ex1.créer_arguments()

#Le calcul de l'intégrale exact
I_exacte = round(ex1.integration_exacte(a, b, p1, p2, p3, p4), 5)

#Le calcul de l'intégrale selon la méthodes des rectangles (sans Numpy
I_calcul_base = round(ex1.methode_des_rectangles_basique(n, a, b, p1, p2, p3, p4), 5)
print(f"Pour un nombre de segments de {n}, la valeur calculée avec du python de base est : {I_calcul_base} et la valeur exacte est : {I_exacte} ")

#Fonction calculant l'erreur de l'intégration numérique
erreur_integration = ex1.erreur_integration_num(I_exacte, I_calcul_base)
erreur_integration_prct = round(erreur_integration * 100, 5)
print(f"L'erreur d'intégration est de {erreur_integration} soit environ {erreur_integration_prct} %\n")

#Meme principe mais en vectorisant avec Numpy
I_calcul_numpy = round(ex1.methode_des_rectangles_numpy(n, a, b, p1, p2, p3, p4), 5)
print(f"Pour un nombre de segments de {n}, la valeur calculée avec numpy est : {I_calcul_numpy} et la valeur exacte est : {I_exacte} ")
erreur_integration_numpy = ex1.erreur_integration_num(I_exacte, I_calcul_numpy)
erreur_integration_prct_numpy = round(erreur_integration_numpy * 100, 5)
print(f"L'erreur d'intégration est de {erreur_integration_numpy} soit environ {erreur_integration_prct_numpy}%\n")

# Evaluation du temps d'éxecution pour les deux méthodes
temps_calcul_numpy = timeit('ex1.Convergence_selon_n(500,a,b,p1,p2,p3,p4,\'numpy\')', globals=globals(), number=100)
temps_calcul_base = timeit('ex1.Convergence_selon_n(500,a,b,p1,p2,p3,p4,\'base\')', globals=globals(), number=100)
print(f'Le temps de calcul de la convergence pour n=500 en utilisant du python de base est de {temps_calcul_base} secondes')
print(f'Le temps de calcul de la convergence pour n=500 en utilisant numpy est de {temps_calcul_numpy} secondes')
print(f'Numpy est {round(temps_calcul_base / temps_calcul_numpy)} fois plus rapide\n')

#Cette fonction trace les deux intégrales (exacte et méthode des rectangles) pour aider l'interprétation de la convergence pour n = 500
ex1.tracer_Integrales_segment(I_exacte, 500, a, b, p1, p2, p3, p4)

#Cette fonction trace la convergence en fonction du nombre de segments
ex1.tracer_convergence(70, a, b, p1, p2, p3, p4)

#Cette fonction trace l'erreur en fonction du nombre de segments
ex1.tracer_erreur_num_segments(20, a, b, p1, p2, p3, p4)
