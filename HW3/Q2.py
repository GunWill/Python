from Q1 import vandermonde
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def lagrange(points):
    x = points[:, 0] # all x values
    y = points[:, 1] # all y values
    n = len(x) # Number of points
    total = Polynomial([0, 0]) #Running sum of y * l, starting at 0

    for i in range(n):
        Li = Polynomial([1, 0])

        for j in range(n):
            if j != i: #Skip j = i so no divide by 0
                Li = Li * Polynomial([-x[j], 1.0]) / (x[i] - x[j])
        total = total + y[i] * Li
    return total #Return Lagrange

f = lambda x: np.exp(-x) * np.cos(3 * x) #Comparison with Vandermonde from Q1

xs = np.linspace(0, 3, 8)
pts = np.column_stack((xs, f(xs)))

pv = vandermonde(pts)
pl = lagrange(pts)

xf = np.linspace(0, 3, 500)
print("Max diff:", np.max(np.abs(pv(xf) - pl(xf))))

plt.figure(figsize=(8,5)) #Plotting
plt.plot(xf, f(xf), 'k', lw=2, label = 'True f(x)')
plt.plot(xf, pv(xf), 'b--', lw=2, label = "Vandermonde")
plt.plot(xf, pl(xf), 'r:', lw=3, label = 'Lagrange')
plt.legend()
plt.grid(True)
plt.title('Lagrange vs Vandermonde')
plt.show()

#As I'm reusing my vandermonde from Q1, the first sine output also prints, apologies for any confusion