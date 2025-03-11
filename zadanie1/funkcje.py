import numpy as np
def wybor_funkcji(literka):
    if (literka=='A' or literka=='a'):
        return lambda x: x**3 + 5*x**2 - 2*x - 10
    if(literka=='B' or literka=='b'):
        return lambda x: 3*x**3 + 3*x**2 - 18*x
    if(literka=='C' or literka=='c'):
        return np.sin
    if(literka=='D' or literka=='d'):
        return np.cos
    if(literka=='E' or literka=='e'):
        return lambda x: 2**x
    if(literka=='F' or literka=='f'):
        return lambda x: (1/2)**x
    if(literka=='G' or literka=='g'):
        return lambda x: np.sin((1/2)*x)
    if(literka=='H' or literka=='h'):
        return lambda x: np.cos(2*x + 1)