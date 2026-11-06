import numpy as np

v1 = 10
R1 = 1000
R2 = 1000
R3 = 9000
R4 = 10000

A=np.array([
    [1/R1 + 1/R3, -1/R1], 
           [-1/R1, 1/R1 + 1/R2 + 1/R4]])

b = np.array([0, v1 / R2])

v = np.linalg.solve(A, b)
va, vb = v
print(f"Node voltages from numpy: va = {va:.4f}V, vb = {vb:.4f}V")

def gaussian_elim(A, b):
    A= A.astype(float)
    b = b.astype(float)
    n = len(b)

    for k in range(n):
        maxindex = abs(A[k:, k]).argmax()+k #Looks at all entries in column k, takes abs value, returns index of largest
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular") #If pivot is 0, raise an error
        if maxindex !=k:
            A[[k, maxindex]] = A[[maxindex, k]]
            b[[k, maxindex]] = b[[maxindex, k]] #Swaps rows
        
        for row in range(k+1, n):
            mult = A[row, k] / A[k, k]
            A[row, k:] -= mult* A[k,k:]
            b[row]-= mult * b[k] #Eliminates to create upper diag.

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x #Back substitution for solutions

v_gauss = gaussian_elim(A.copy(), b.copy())
print(f"Homemade node voltages: va = {v_gauss[0]:.4f}V, vb = {v_gauss[1]:.4f}V")

if(va == v_gauss[0] and vb==v_gauss[1]):
    print("Voltages match!")
else:
    print("Voltages are off")
