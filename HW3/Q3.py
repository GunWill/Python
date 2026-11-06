import numpy as np
import matplotlib.pyplot as plt

wl = np.array([6563, 6439, 5890, 5338, 5086, 4861, 4340, 3988], float)
ri = np.array([1.50883, 1.50917, 1.51124, 1.51386,
               1.51534, 1.51690, 1.52136, 1.52546])

def lagrange(xn, yn): #Computes lagrange of given points
    def P(x):
        x = np.asarray(x, float)
        total = np.zeros_like(x)
        for i in range(len(xn)):
            Li = np.ones_like(x)
            for j in range(len(xn)):
                if j != i:
                    Li *= (x - xn[j]) / (xn[i] - xn[j])
            total += yn[i] * Li
        return total
    return P
P = lagrange(wl, ri)

def bisection(f, a, b, tol=1e-6, iter=100): #I chose bisection, same implementation as previous
    fa, fb, = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must not have same sign")
    for k in range(iter):
        c = (a + b) / 2
        fc = f(c)

        if fc == 0 or (b-a) / 2 < tol:
            return c, k+1

        if fa*fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a + b) / 2, iter

target = 1.510
f = lambda x: float(P(x) - target) #We want f(x) = 0

root, iters = bisection(f, 5890, 6439, tol=1e-6)
print(f"Wavelength for n= {target}: {root:.4f} ({iters} iterations)")
print(f"Check: P(root) = {float(P(root)):.10f}")

xp = np.linspace(3988, 6563, 500) #Plots lagrange interpolation of func, bisection implementation prints in terminal
plt.figure(figsize=(8,5))
plt.plot(xp, P(xp), label = 'Lagrange')
plt.plot(wl, ri, 'ko', label = 'Data')
plt.plot(root, target, 'r*', ms=12, label=f'n=1.510 at {root:.1f}')
plt.xlabel('Wavelength')
plt.ylabel('Refractive index')
plt.title('Refractive index of borosilicate glass')
plt.legend()
plt.grid(True)
plt.show()