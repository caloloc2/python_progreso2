import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

f = lambda x: 2.0*np.exp(-2.0*x) # crea la funcion
x = np.arange(0.01, 3.0, (3.0-0.01)/10000) # crea valores de x para la funcion

fx = f(x) # valores de y segun x


ch= st.chi2(4) # chi-squared
h = lambda x: f(x)/ch.pdf(x) # h-function





# M=.3 # scale factor
# u1 = np.random.normal(10000)*15 # uniform random samples scaled out
# u2 = np.random.normal(10000)    # uniform random samples

# print u1
# print u2

# print f(u1)

idx= np.argwhere(u2<=f(u1)/M)[0] # rejection criterion
# v = u1[idx]

# print v