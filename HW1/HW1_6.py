import numpy as np
import matplotlib.pyplot as plt

def f(x): #Function
    return -0.3 * x**4 + 1.8 * x**3 - 1.2 * x**2 + x

def neg_f(x): #Minimize f(x) to find maxima
    return -f(x)
def golden(func, xl, xu, es=1, iter = 100):
    phi = (1 + np.sqrt(5)) / 2

    d = (phi - 1) * (xu - xl) #Interior points for golden section search
    x1 = xu - d
    x2 = xl + d

    iters = 0
    while True:
        iters +=1
        if neg_f(x1) < neg_f(x2): #Compare function values
            xu = x2
        else:
            xl = x1

        d = (phi - 1) * (xu - xl) #Updated Interval
        x1_old = x1
        x1 = xu - d
        x2 = xl + d

        if x2!= 0: #Calculating error
            err = abs((x2 - x1) / x2) * 100
        else:
            err = 0
        if err < es or iters >= iter:
            break
    return (xl + xu) / 2, iters, err

def parabolic(x1, x2, x3, iter = 100):
    for i in range(iter):
        d1 = x2 - x1 #slopes
        d2 = x3 - x2

        h1 = (neg_f(x2) - neg_f(x1)) / d1
        h2 = (neg_f(x3) - neg_f(x2)) / d2

        denom = (h2 - h1) / (d2 + d1) #calculate denominator

        if denom == 0:
            break
        x_new = x2 - (d1 * h2 - d2 * h1) / (2*denom) #Calculate new estimate for min -f(x)

                # Add this bracketing check
        if x_new < x1 or x_new > x3:
            # If outside, fall back to midpoint
            x_new = x2 + 0.5 * (x3 - x1) * (1 if x2 > (x1+x3)/2 else -1)


        if x_new > x2: #Update points
            if neg_f(x_new) < neg_f(x2):
                x1 = x2
                x2 = x_new
            else:
                x3 = x_new
        else:
            if neg_f(x_new) < neg_f(x2):
                x3 = x2
                x2 = x_new
            else:
                x1 = x_new
    return x2, neg_f(x2)

xl, xu = -2, 4
root_gs, iters_gs, err_gs = golden(neg_f, xl, xu, es=1)
max_val_gs = f(root_gs)

print(f"Golden-Section Search:")
print(f"Root GS: {root_gs:.6f}")
print(f"Max Value: {max_val_gs:.6f}")
print(f"Iterations: {iters_gs}")
print(f"Final Error: {err_gs:.4f}")

x1, x2, x3 = -2, 1, 2
root_pi, min_val_pi = parabolic(x1, x2, x3, iter=5)
max_val_pi = -min_val_pi

print(f"Parabolic Interpolation:")
print(f"Root Parab.: {root_pi:.6f}")
print(f"Max Value: {max_val_pi:.6f}")

x = np.linspace(-2, 4, 400)
plt.figure(figsize=(10, 6))
plt.plot(x, f(x), label='$f(x) = -0.3x^4 + 1.8x^3 - 1.2x^2 + x$', linewidth=2)
plt.plot(root_gs, max_val_gs, 'ro', markersize=12, label=f'Golden-Section Max')
plt.plot(root_pi, max_val_pi, 'bs', markersize=12, label=f'Parabolic Max')
plt.grid(True)
plt.legend()
plt.title('Golden section vs Parabolic')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()