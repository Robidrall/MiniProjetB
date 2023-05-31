import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit
import time

def créer_arguments():
    a = input(int("Entrez le premier point de l'intervalle"))
    b = input(int("Entrez le dernier point de l'intervalle"))
    p1 = input(int("Entrez "))
    p2 = input(int("Entrez "))
    p3 = input(int("Entrez "))
    p4 = input(int("Entrez "))
    x =  input(int("Entrez "))
    return a, b, p1, p2, p3, p4, x

def integration_exacte (a,b,p1,p2,p3,p4):
    I_exacte = p1*(b-a)+p2*(b**2-a**2)/2 +p3*(b**3-a**3)/3 + p4*(b**4-a**4)/4
    return I_exacte
       
def det_solution_analytique(x,p1,p2,p3,p4):
    return p1 + p2*x +p3*x**2 + p4*x**3

def methode_des_rectangles(n,p1,p2,p3,p4,a,b):
   I_calc = 0
   pas = (b - a) / n
   intervalle = [a + i * pas for i in range(n + 1)]
   for i in range(n):
        aire = det_solution_analytique(intervalle[i] + (intervalle[i + 1] - intervalle[i])/2, p1, p2, p3, p4) * (intervalle[i + 1] - intervalle[i])
        I_calc += aire
   return I_calc

def erreur_integration_num (valeur_exacte, valeur_calcule):
    erreur = abs(valeur_exacte-valeur_calcule)/valeur_exacte
    return erreur

def Convergence_selon_n (n,p1,p2,p3,p4):
    return round(100*erreur_integration_num(integration_exacte (-2,3,p1,p2,p3,p4),methode_des_rectangles(n,p1,p2,p3,p4))/integration_exacte (-2,3,p1,p2,p3,p4),5)

p1=5
p2=2
p3=4
p4=2
a = -2
b = 3
n = 10

I_exacte = round(integration_exacte (a,b,p1,p2,p3,p4),2)
I_calc = round(methode_des_rectangles(n,p1,p2,p3,p4,a,b),2)
print(f"Pour un nombre de segments de {n}, la valeur calculée est : {I_calc} et la valeur exacte est : {I_exacte} ")

erreur_integration = erreur_integration_num(I_exacte, I_calc)
erreur_integration_prct = round(erreur_integration/100,5)
print(f"La valeur d'intégration est de {erreur_integration} soit environ {erreur_integration_prct} pourcent")

#print(Convergence_selon_n(15,p1,p2,p3,p4))
#print(Convergence_selon_n(50,p1,p2,p3,p4))
#print(Convergence_selon_n(500,p1,p2,p3,p4))
#print(timeit('Convergence_selon_n(500,p1,p2,p3,p4)',globals=globals(),number=1))








