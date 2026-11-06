import numpy as np
import matplotlib.pyplot as plt

def f1(x): #function 1
    return -0.87 * x**2 + 1.65 * x + 8.25

def deriv_f1(x): #Derivative of f1
    return -1.74 * x + 1.65

def f2(x):#function 2
    return -1.9 + 6.31 * x -3.7 * x**2 + 0.7 * x**3
def deriv_f2(x):#derivative of function2
    return 6.31 - 7.4 * x + 2.1 * x**2

def nr(func, deriv, a, tol=1e-8, iter=100):
    errors = []
    x = a
    for i in range(iter):
        funct = func(x)
        der = deriv(x)
        if der == 0:
            return "deriv = 0, no solution"
        x_new = x - funct / der #Determining error via NR method
        err = abs(x_new - x) #Calculating absolute error at x
        errors.append(err)

        if err < tol: #If error is less than tolerance, return answers
            return x_new, i + 1, errors
        x = x_new
    return x, iter, errors

root1, iter1, err1 = nr(f1, deriv_f1, 0)
print(f"Root1:{root1}, iter1={iter1}")
root2, iter2, err2 = nr(f2, deriv_f2, 0)
print(f"Root2={root2}, iter2={iter2}")

# Plot f1(x), (same method as Q1)
x = np.linspace(-5, 5, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, f1(x), label='$f_1(x) = -0.87x^2 + 1.65x + 8.25$', linewidth=2)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f1(x)')
plt.legend()
plt.show()

# Plot f2(x)
plt.figure(figsize=(10, 6))
plt.plot(x, f2(x), label='$f_2(x) = -1.9 + 6.31x - 3.7x^2 + 0.7x^3$', linewidth=2)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f2(x)')
plt.legend()
plt.show()