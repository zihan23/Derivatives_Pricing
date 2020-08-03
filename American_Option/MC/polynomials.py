import numpy as np

def constructX(x, type_of_polynomial):
    if isinstance(x, np.ndarray):
        len1 = len(x)
    else:
        len1 = 1
    if type_of_polynomial.lower() == 'chebychev_firstkind':
        xX = np.ones((len1, 6))
        xX[:, 1] = x
        xX[:, 2] = 2*x**2 - 1
        xX[:, 3] = 4*x**3 - 3*x
        xX[:, 4] = 8*x**4 - 8*x**2 + 1
        xX[:, 5] = 16*x**5 - 20*x**3 + 5*x
    elif type_of_polynomial.lower() == 'chebychev_secondkind':
        xX = np.ones((len1, 6))
        xX[:, 1] = 2*x
        xX[:, 2] = 4*x**2-1
        xX[:, 3] = 8*x**3 - 4*x
        xX[:, 4] = 16*x**4 - 12*x**2 + 1
        xX[:, 5] = 32*x**5 - 32*x**3 + 6*x
    elif type_of_polynomial.lower() == 'laguerre':
        xX = np.ones((len1, 5))
        xX[:, 1] = -x + 1
        xX[:, 2] = (x**2 - 4*x + 2)/2
        xX[:, 3] = (-x**3 + 9*x**2 - 18*x + 6)/6
        xX[:, 4] = (x**4 - 16*x**3 + 72*x**2 - 96*x + 24)/24
    if len1 == 1:
        xX = xX[0]
    return xX