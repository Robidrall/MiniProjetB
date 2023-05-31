import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit
import time

def integration_exacte (a,b,p1,p2,p3,p4): 
    return p1*(b-a)+p2*(b**2-a**2)/2 +p3*(b**3-a**3)/3 + p4*(b**4-a**4)/4
       
def det_solution_analytique(x,p1,p2,p3,p4):
    return p1 + p2*x +p3*x**2 + p4*x**3

def methode_des_rectangles(n,p1,p2,p3,p4):
   somme = 0
   a = -2
   b = 3
   pas = (b - a) / n
   intervalle = [a + i * pas for i in range(n + 1)]
   for i in range(n):
        aire = det_solution_analytique( intervalle[i]+ (intervalle[i + 1] - intervalle[i])/2,p1,p2,p3,p4) * (intervalle[i + 1] - intervalle[i])
        somme += aire
   return somme

def erreur_integration_num (valeur_exacte, valeur_calcule):
    erreur= valeur_exacte-valeur_calcule
    return erreur

def Convergence_selon_n (n,p1,p2,p3,p4):
    return round(100*erreur_integration_num(integration_exacte (-2,3,p1,p2,p3,p4),methode_des_rectangles(n,p1,p2,p3,p4))/integration_exacte (-2,3,p1,p2,p3,p4),5)

p1=5
p2=2
p3=4
p4=2

print(Convergence_selon_n(15,p1,p2,p3,p4))
print(Convergence_selon_n(50,p1,p2,p3,p4))
print(Convergence_selon_n(500,p1,p2,p3,p4))
print(timeit('Convergence_selon_n(500,p1,p2,p3,p4)',globals=globals(),number=1))








