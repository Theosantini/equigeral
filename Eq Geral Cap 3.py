# Simular modelo EGC CAP 3
import numpy as np
import scipy
import scipy.optimize as opt
i = 1

k = 1

h = 1

j = i

dotacao = np.array([[30, 20], [20, 5]])

beta = np.array([[0.3, 0.6], [0.7, 0.4]])

A = np.array([[0.2, 0.5],[0.3, 0.25]])

alfa = np.array([[0.8, 0.4], [0.2, 0.6]])

va = np.transpose(np.array([0.5, 0.25]))

# Exemplo otimização 1

objective_fcn = lambda x: x[0]**2 + x[0]*x[1]

constraint = [{'type':'eq', 'fun' : lambda x: x[0]**3 + x[0]*x[1] - 100},
              {'type':'ineq','fun' : lambda x: x[0]**2 + x[1] - 50}]

x0 = [1, 1]

bounds = [(-100,100),(-100,100)]

result = scipy.optimize.minimize(objective_fcn, x0, method = 'SLSQP',
                                 bounds=bounds, constraints = constraint)

## Exemplo 2: max u((x1**aplpha)*(x2**(1-alpha))) sa p1x1 + p2x2 <= 1, x1>=0, x2>=0

def utility(x, p, alpha):
    return -1.0 * (x[0]**alpha)*(x[1]**(1-alpha))

def utility_constraints(x, p, alpha):
    return np.array([x[0], x[1], 1- p[0]*x[0] - p[1]*x[1]])

p = np.array([1.0,1.0])
alpha = 1.0/3
x0 = np.array([.4,.4])
opt.fmin_slsqp(utility, x0, f_ieqcons=utility_constraints, args=(p, alpha))





