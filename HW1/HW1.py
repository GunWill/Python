import numpy as np
import matplotlib.pyplot as plt

def funct(theta): ##Defines the function described in problem 1
    return np.sin(theta) - theta**2

theta = np.linspace(-2, 2, 100) #Start and end of linspace, with # of samples
plt.figure(figsize=(10,6))
plt.plot(theta, funct(theta), label='$sin(theta) - theta^2$') #Actual plot, x, y, and label
plt.axhline(0, color = 'black', linewidth = 1)
plt.axvline(0, color = 'black', linewidth = 1)
plt.grid(True)
plt.xlabel('$theta$')
plt.ylabel('funct($theta$)')
plt.legend() #Plots label from earlier
plt.title('Plot of $sin(theta) - theta^2$')
plt.show() #Shows plot

def bisection(func, a,  b, tol= (1*(10e-8)), iter=100): #Bisection function def
    for i in range(iter): #Iterates 100 times, (changeable)
        c = (a+b)/2 #Defines c as the halfway point between bracketing values
        if func(a) * func(b) >=0:
            return "Bisection method fails"
        if func(c) == 0 or (b-a) / 2 < tol: #If c is exactly the root or values are within the tolerance, return c immediately
            break
        if func(a) * func(c) < 0: #If the a * b is negative, bring b closer to a
            b = c
        else: #If the a*b is positive, bring a closer to b
            a = c
    return c
root1 = bisection(funct, -.25, .25)
root2 = bisection(funct, .75, 1.25)
print(f"The first root is ~{root1}")
print(f"The second root is ~{root2}")
    