# Simular modelo EGC CAP 3
from numpy import *
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


def eq(pyw, *p1):
    p1 = numeraire
    p2 = pyw[0]
    y1 = pyw[1]
    y2 = pyw[2]
    w1 = pyw[3]
    w2 = pyw[4]

    eqc = empty((5))

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

    return eqc


numeraire = (1)

pyw0 = array([0.8, 2, 2, 0.8, 0.8])

pyw = fsolve(eq, pyw0)

print(pyw)
