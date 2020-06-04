# Simular modelo EGC CAP 3
from numpy import *
import scipy
import scipy.optimize as opt
from scipy.optimize import *

i = 1

k = 1

h = 1

j = i

dotacao = array([[30, 20], [20, 5]])

beta = array([[0.3, 0.6], [0.7, 0.4]])

A = array([[0.2, 0.5], [0.3, 0.25]])

alfa = array([[0.8, 0.4], [0.2, 0.6]])

va = array([0.5, 0.25])


def eq(pyw):
    p1 = pyw[0]
    p2 = pyw[1]
    y1 = pyw[2]
    y2 = pyw[3]
    w1 = pyw[4]
    w2 = pyw[5]

    eqc = empty((6))

    eqc[0] = beta[0, 0] * (w1 * dotacao[0, 0] + w2 * dotacao[1, 0]) / p1 + \
            beta[0, 1] * (w1 * dotacao[0, 1] + w2 * dotacao[1, 1]) / p1 + \
            A[0, 0] * y1 + A[0, 1] * y2 - y1
    eqc[1] = beta[1, 0] * (w1 * dotacao[0, 0] + w2 * dotacao[1, 0]) / p2 + \
            beta[1, 1] * (w1 * dotacao[0, 1] + w2 * dotacao[1, 1]) / p2 + \
            A[1, 0] * y1 + A[1, 1] * y2 - y2
    eqc[2] = (alfa[0, 0] * (w2 / w1) ** alfa[1, 0]) * y1 * va[0] + (alfa[0, 1] * (w2 / w1) ** alfa[1, 1]) * y2 * va[1] - \
            dotacao[0, 0] - dotacao[0, 1]
    eqc[3] = (alfa[1, 0] * (w1 / w2) ** alfa[0, 0]) * y1 * va[0] + (alfa[1, 1] * (w1 / w2) ** alfa[0, 1]) * y2 * va[1] - \
            dotacao[1, 0] - dotacao[1, 1]
    eqc[4] = p1 - (w1 ** alfa[0, 0]) * (w2 ** alfa[1, 0]) * va[0] - p1 * A[0, 0] - p2 * A[1, 0]

    eqc[5] = p2 - (w1 ** alfa[0, 1]) * (w2 ** alfa[1, 1]) * va[1] - p1 * A[0, 1] - p2 * A[1, 1]

    return eqc


pyw0 = array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])

pyw = fsolve(eq, pyw0)

print(pyw)



# Exemplo otimização 1

# objective_fcn = lambda x: x[0]**2 + x[0]*x[1]

# constraint = [{'type':'eq', 'fun' : lambda x: x[0]**3 + x[0]*x[1] - 100},
#              {'type':'ineq','fun' : lambda x: x[0]**2 + x[1] - 50}]

# x0 = [1, 1]

# bounds = [(-100,100),(-100,100)]

# result = scipy.optimize.minimize(objective_fcn, x0, method = 'SLSQP',
#                                bounds=bounds, constraints = constraint)

## Exemplo 2: max u((x1**aplpha)*(x2**(1-alpha))) sa p1x1 + p2x2 <= 1, x1>=0, x2>=0

# def utility(x, p, alpha):
#   return -1.0 * (x[0]**alpha)*(x[1]**(1-alpha))

# def utility_constraints(x, p, alpha):
#   return np.array([x[0], x[1], 1- p[0]*x[0] - p[1]*x[1]])

# p = np.array([1.0,1.0])
# alpha = 1.0/3
# x0 = np.array([.4,.4])
# opt.fmin_slsqp(utility, x0, f_ieqcons=utility_constraints, args=(p, alpha))
