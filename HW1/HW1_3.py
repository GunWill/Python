import numpy as np
import matplotlib.pyplot as plt

def g(x): #Fixed point function g(x)
    return np.sin(x**2)
def f(x): #original function
    return np.sin(x**2) - x

def fp(func, a, tol=1e-4, iter=100):
    errors = []
    x = a
    for i in range(iter):
        x_new = func(x)
        err = abs(x_new - x) #calculating abs. error
        errors.append(err)

        if err < tol:
            return x_new, i + 1, errors #If error is within tolerance, print root, iteration number, and errors
        x = x_new
    return x, iter, errors

root_fp, iter_fp, error_fp = fp(g, 0.5)
print(f"Root: {root_fp}")
print(f"Iterations: {iter_fp}")

plt.figure(figsize = (10, 6))
plt.semilogy(error_fp, label = 'Fixed point errors', marker = 'o')
plt.xlabel('Iteration')
plt.ylabel('Abs. Error')
plt.title("Absolute error vs Iteration")
plt.legend()
plt.show()