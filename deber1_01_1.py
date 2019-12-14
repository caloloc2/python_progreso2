import numpy as np
from matplotlib import pyplot as plt
import numpy.random as ra
from funciones import ITS, RM

# valores de x y f(x) de la funcion a analizar
x = np.arange(-100, 0, (3.0-0.01)/100) # crea valores de x para la funcion
f = lambda x: np.exp(x*2)

datos = ITS(x, f(x))

datos = ((np.array(datos) - 1) / 1).astype(int)
times = np.arange(1, 6, 1)
lc = np.bincount(datos, minlength=len(times))

plot1, = plt.plot(lc/float(sum(lc)), 'r--', label='Assigned energies')
#plot2, = plt.plot(prob,'g',label='Original espectro')
plt.xlabel('Energies')
plt.ylabel('Probability')
plt.legend(handles=[plot1])
plt.show()
