import numpy as np
import matplotlib.pyplot as plt
import timeit
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
   print(intervalle)
   for i in range(n):
        aire = det_solution_analytique( intervalle[i]+ (intervalle[i + 1] - intervalle[i])/2,p1,p2,p3,p4) * (intervalle[i + 1] - intervalle[i])
        somme += aire
   return somme


p1=5
p2=2
p3=4
p4=2
somme = methode_des_rectangles(10,p1,p2,p3,p4)
print(somme)

somme = methode_des_rectangles(100,p1,p2,p3,p4)

print(somme)


valeur_reelle = integration_exacte(-2,3,5,2,4,2)
print(valeur_reelle)



