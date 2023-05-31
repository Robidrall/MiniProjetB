import numpy as np
import matplotlib.pyplot as plt
import timeit
import time


def det_solution_analytique(x):
    p1 = 5
    p2 = 2
    p3 = 4
    p4 = 2
    return p1 + p2*x +p3*x**2 + p4*x**3

def methode_des_rectangles(n):
   somme = 0
   a = -2
   b = 3
   pas = (b - a) / n
   intervalle = [a + i * pas for i in range(n + 1)]
   print(intervalle)
   for i in range(n):
       aire = det_solution_analytique(intervalle[i + 1] - intervalle[i]) * (intervalle[i + 1] - intervalle[i])
       if aire > 0:
           somme += aire
       else:
           somme -= aire
   return somme

somme = methode_des_rectangles(10)
print(somme)



