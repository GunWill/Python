import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def vandermonde(points):
    x = points[:, 0] #X values
    y = points[:, 1] #Y values
    V = np.vander(x, increasing = True) #Creates and prints Vandermonde matrix
    #print(V)
    coeffs = np.linalg.solve(V,y) #Computes coeffs of matrix by V*c=y
    #print("Coefficients:", coeffs)
    return Polynomial(coeffs) #return as polynomial object

def real(x):
    return np.sin(2 * np.pi * x)

plt.figure(figsize = (12, 8))

n_val = range(5, 101, 5)
x_true = np.linspace(0, 2, 1000)
y_true = real(x_true)

plt.plot(x_true, y_true, label = "True function", color='black', linewidth=2)



for n in n_val:
    x_interp = np.linspace(0, 2, n)
    y_interp = real(x_interp)

    points = np.column_stack((x_interp, y_interp))
    poly = vandermonde(points)
    y_pred = poly(x_true)
    plt.plot(x_true, y_pred, label=f"n = {n}", linestyle="--")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Vandermonde interpolation of sin(2pix)")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(True)
plt.tight_layout()
plt.ylim(-5, 5)
plt.show()
