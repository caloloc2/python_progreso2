import scipy.stats as ss
import matplotlib.pyplot as plt
import numpy as np

ejemplares = 50 # numero de ejemplares
fx = [0.022, 0.033, 0.030] # valores de la funcion
costo = 0.5

X = ss.binom(ejemplares, fx[0]) # crea la distribucion del valor asignado
pr = X.sf(1) # probabilidad de vender todos los ejemplares

print "Probabilidad de vender todos =", (pr*100),"%"
porc = (pr*50) # ejemplares al dia
rest = 50 - porc
print "Ejemplares no vendidos al dia =", rest
neto = porc * costo
print "Ingreso neto esperado $ ", neto

x = np.arange(10)
plt.plot(x,X.pmf(x),"bo")
plt.vlines(x,0,X.pmf(x),"b")
plt.show()