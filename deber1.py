import numpy as np # importa libreria numpy
from matplotlib import pyplot as plt # libreria para graficar
from funciones import ITS, RM # importa funciones del archivo 'funciones.py'

min, max = 2, 3 # limites de la funcion a analizar
step = 0.1 # numero de muestras
x = np.arange(min, max, step) # crea valores de x para la funcion

# aqui se configura la funcion a analizar, seleccionar segun el ejercicio
# la funcion y dominio o rango de valores que se especifican (min, max)
#f = lambda x: np.exp(2*x)       # de -inf a 0
#f = lambda x: np.exp(-1*2*x)   # de 0.01 a + inf
f = lambda x: 0.5*(x-2)        # de 2 a 3
#f = lambda x: 0.5*(2-(x/3))    # de 3.01 a 6

datos = ITS(x, f(x)) # analiza la funcion de probabilidad

# grafica la distribucion encontrada
times = np.arange(1, 10, 1)
lc = np.bincount(datos, minlength=len(times))
plot1, = plt.plot(lc/float(sum(lc)), 'r--', label='f(x)')
plt.xlabel('Eje x')
plt.ylabel('Probabilidad')
plt.legend(handles=[plot1])
plt.show()
