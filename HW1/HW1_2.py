import numpy as np
import matplotlib.pyplot as plt
import math

def funct(theta):
    return np.cos(theta) - theta #finding root of cos(theta) = theta can be rewritten as such

def bisection(func, a, b, tol = 1*(10**-4), iter = 100):
    errors = []
    if func(a) * func(b) >= 0:
        return "Bisection method fails"
    c = a
    iterations = 0
    errors = []
    for i in range(iter):
        c_prev = c
        c = (a + b) / 2
        iterations += 1
        if c!=0:
            err = abs((c - c_prev) / c) * 100
        else:
            err = 0
        errors.append(err)
        if err < tol:
            break
        if abs(func(c)) < tol:
            break
        if abs(c - c_prev) < tol:
            break

        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c, iterations, errors
root_b, iter_b, error_b = bisection(funct, 0, np.pi)
print(f"Bisection root is {root_b}")
print(f"# of Bisection iterations = {iter_b}")

def rf(func, a, b, tol = 1e-4, iter = 100):
    if func(a) * func(b) >= 0:
        return "Regula Falsi not work"
    errors = []
    c = a
    iterations = 0
    for i in range(iter):
        c_prev = c
        c = (a*func(b) - b* func(a)) / (func(b) - func(a))
        iterations +=1

        if c!= 0:
            err = abs((c - c_prev) / c) * 100
        else:
            err = 0
        errors.append(err)
        if err < tol:
            break
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c, iterations, errors
root_rf, iter_rf, error_rf = rf(funct, 0, np.pi)
print(f"RF Root is {root_rf}")
print(f"RF # of iterations is {iter_rf}")

plt.figure(figsize = (10, 6))
plt.semilogy(error_b, label = 'Bisection errors', marker = 'o')
plt.semilogy(error_rf, label = "Regula Falsi errors", marker = 's')
plt.xlabel("Iteration")
plt.ylabel("Error")
plt.title("Comparison of Bisection and Regula Falsi errors for cos(theta) = theta")
plt.legend()
plt.show()