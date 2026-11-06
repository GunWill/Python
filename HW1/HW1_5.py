import numpy as np
import matplotlib.pyplot as plt

def f(theta):
    return 3* np.sin(theta) ** 2 + np.cos(theta) - theta **3 + 9

def deriv_f(theta): #deriv for NR
    return 3 * np.sin(2*theta) - np.sin(theta) - 3 * theta**2

#Bisection method : Same as Q2
def bisect(func, a, b, tol = 1e-4, iter = 100):
    values = []
    if func(a) * func(b) >= 0:
        return "Bisection method fail"
    c = a
    for i in range(iter):
        c_prev = c
        c = (a + b) / 2
        values.append(c)
        if abs(c - c_prev) < tol: #If difference between old & new is less than tol, return root & list
            break
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c, values
#RF method, same as Q2
def rf(func, a, b, tol = 1e-4, iter = 100):
    values = []
    if func(a) * func(b) >= 0:
        return "RF method no work"
    c = a
    for i in range(iter):
        c_prev = c
        c = (a*func(b) - b* func(a)) / (func(b) - func(a)) #Calclate new C via NR method
        values.append(c)
        if abs(c - c_prev) < tol: #If difference between old & new is less than tol, return root & list
            break   
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c, values
def nr(func, deriv, a, tol=1e-4, iter = 100):
    values = []
    x = a
    for i in range(iter):
        x_new = x - func(x) / deriv(x) #Determine new x via NR method
        values.append(x_new)
        if abs(x_new - x) < tol: #If difference between old & new is less than tol, return root & list
            break
        x = x_new
    return x, values

def secant(func, a, b, tol = 1e-4, iter = 100):
    values = []
    for i in range(iter):
        f_a = func(a)
        f_b = func(b)
        if f_a == f_b:
            break
        x_new = a - f_a * (b - a) / (f_b - f_a) #Determine new value via Secant method
        values.append(x_new)
        if abs(x_new - b) < tol: #If difference between old & new is less than tol, return root & list
            break
        a = b
        b = x_new
    return b, values

root_bisect, vals_bisect = bisect(f, 2, 3) #Assigning outputs of each function
root_rf, vals_rf = rf(f, 2, 3)
root_nr, vals_nr = nr(f, deriv_f, 2.5)
root_sec, vals_sec = secant(f, 2, 3)

print(f"Bisection Root: {root_bisect}") #Printing roots for each function
print(f"Regula Falsi Root: {root_rf}")
print(f"Newton-Raphson Root: {root_nr}")
print(f"Secant Root: {root_sec}")

plt.figure(figsize=(10, 6)) #Plotting values at each iteration
plt.plot(vals_bisect, label='Bisection', marker='o')
plt.plot(vals_rf, label='Regula Falsi', marker='s')
plt.plot(vals_nr, label='Newton-Raphson', marker='^')
plt.plot(vals_sec, label='Secant', marker='d')
plt.xlabel('Iteration')
plt.ylabel('Values')
plt.title('Convergence of All Methods')
plt.grid(True)
plt.legend()
plt.show()