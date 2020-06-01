# Simular modelo EGC CAP 3
import numpy as np

i = 1

k = 1

h = 1

j = i

dotacao = np.array([[30, 20], [20, 5]])

beta = np.array([[0.3, 0.6], [0.7, 0.4]])

A = np.array([[0.2, 0.5],[0.3, 0.25]])

alfa = np.array([[0.8, 0.4], [0.2, 0.6]])

va = np.transpose(np.array([0.5, 0.25]))