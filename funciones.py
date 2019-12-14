import numpy as np
from matplotlib import pyplot as plt
import numpy.random as ra

def ITS(x, y): # parametro es la funcion de distribucion de probabilidad PDF
    xs = np.array(x) # valores en x
    ys = np.array(y) # valores en y [f(x)]

    prob = ys/float(sum(ys)) # probabilidad
    cum_prob = np.cumsum(prob) # obtiene funcion de distribucion acumulativa CDF

    # Generamos numeros aleatoreos entre 0 y 1
    N = 10000 # numero de muestras
    R = ra.uniform(0, 1, N) # numeros aleatoreos

    gen_xs = [int(xs[np.argwhere(cum_prob == min(cum_prob[(cum_prob - r) > 0]))]) for r in R]

    return gen_xs

def RM(pdf,n=1000,xmin=0,xmax=1):
    # Calculates the minimal and maximum values of the PDF in the desired  
    # interval. The rejection method needs these values in order to work  
    # properly.  
    x=np.linspace(xmin,xmax,1000)  
    y=pdf(x)  
    pmin=0.  
    pmax=y.max()  

    # Counters  
    naccept=0  
    ntrial=0  

    # Keeps generating numbers until we achieve the desired n  
    ran=[] # output list of random numbers  
    while naccept<n:  
        x=np.random.uniform(xmin,xmax) # x'  
        y=np.random.uniform(pmin,pmax) # y'  

    if y<pdf(x):  
        ran.append(x)  
        naccept=naccept+1  
    ntrial=ntrial+1  

    ran=np.asarray(ran)  

    return ran,ntrial 