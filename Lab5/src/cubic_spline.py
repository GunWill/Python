import numpy as np

def nat_cubic(x, y, x_eval=None):

    #Convert inputs to numpy float arrays
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    n = len(x) #Number of data points

    if n < 2:
        raise ValueError("Need at least 2 data points for interpolation")

    h = np.diff(x) #Spacing between consecutive x values

    if n == 2:
        M = np.zeros(2) # With only 2 points, both second derivs are 0
    else:
        inner = n - 2 #Number of unknowns

        a = np.zeros(inner) #Buillding tridiagonal system => similar to last lab
        b = np.zeros(inner)
        c = np.zeros(inner)
        d = np.zeros(inner)

        for i in range(inner):
            ii = i + 1 #Map from inner index to original array index

            a[i] = h[ii - 2] if ii > 1 else 0.0 #sub diagonal
            b[i] = 2.0 * (h[ii-2] + h[ii-1]) if ii>1 else 2.0 * h[ii-1] #main diag
            c[i] = h[ii - 1] #Super diag

            if ii > 1: #Right hand side
                d[i] = 6.0 * (
                    (y[ii + 1] - y[ii]) / h[ii - 1]
                    - (y[ii] - y[ii - 1]) / h[ii - 2]
                )
            else:
                d[i] = 6.0 * ((y[ii + 1] - y[ii]) / h[ii - 1]) #For the first eq, use only forward diff

        #Thomas algorithm for solving tridiagonal systems
        c_prime = np.zeros(inner) #Modified super left diag.
        d_prime = np.zeros(inner) #Modified RHS post forward elim

        c_prime[0] = c[0] / b[0]
        d_prime[0] = d[0] / b[0]

        for i in range(1, inner): #Forward elim
            denom = b[i] - a[i] *c_prime[i-1]
            c_prime[i] = c[i] / denom if i< inner - 1 else 0.0
            d_prime[i] = (d[i] - a[i] * d_prime[i-1]) / denom

        M_inner = np.zeros(inner) #Back substitution
        M_inner[-1] = d_prime[-1]

        for i in range(inner -2, -1, -1):
            M_inner[i] = d_prime[i] - c_prime[i] * M_inner[i + 1]

        M = np.zeros(n) #Assemble full M array w zeros at ends
        M[1: -1] = M_inner

    #Evaluate spline @ requested points
    if x_eval is not None:
        x_eval = np.asarray(x_eval, dtype=float)
        result = np.zeros_like(x_eval, dtype=float)

        for idx, xi in enumerate(x_eval): #Evaluates at each requested point
            if xi <= x[0]:    
                seg = 0
            elif xi >= x[-1]:
                seg = n - 2
            else:
                seg = np.searchsorted(x, xi, side = 'right') - 1

            xi_seg = x[seg] #Left endpoint
            hi = h[seg] #Width of segment
            yi = y[seg] #Y-value at left endpoint
            yi1 = y[seg + 1] #Y-value at right endpoint
            Mi = M[seg] #Second deriv at left enpoitn
            Mi1 = M[seg + 1] #Second deriv at right endpoint

            t = (xi - xi_seg) / hi #Normalize

            result[idx] = (
                (1 - t) * yi + t*yi1 + hi*hi * (((1 - t) ** 3 - (1 - t)) / 6 * Mi + (t**3 - t)/6 *Mi1)
            )
        return result
    coeffs = { 'x':x, 'y':y, 'M':M, 'h':h, 'n':n,} #Return coeffs

    a = y[:-1] #Compute coeffs
    b = np.diff(y) / h - h * (2 * M[:-1] + M[1:]) / 6
    c = M[:-1] / 2
    d = np.diff(M) / (6 * h)

    coeffs ['a'] = a
    coeffs ['b'] = b
    coeffs ['c'] = c
    coeffs ['d'] = d    
    return coeffs

def evaluate(coeffs, x_eval):
    x = coeffs['x']
    y= coeffs['y']
    M = coeffs['M']
    h = coeffs['h']
    n = coeffs['n']

    x_eval = np.asarray(x_eval, dtype=float) #Convert eval points to numpy array
    result = np.zeros_like(x_eval, dtype=float)

    for idx, xi in enumerate(x_eval): #Evaluate spline at each point
        if xi<= x[0]:
            seg = 0
        elif xi >= x[-1]:
            seg = n-2
        else:
            seg = np.searchsorted(x, xi, side = 'right') - 1

        xi_seg = x[seg]
        hi = h[seg]
        yi = y[seg]
        yi1 = y[seg + 1]
        Mi = M[seg]
        Mi1 = M[seg + 1]

        t = (xi - xi_seg) / hi

        result[idx] = ((1-t) * yi + t*yi1 + hi*hi* ((1 - t) ** 3 - (1-t)) / 6 * Mi + (t**3 - t) / 6 * Mi1)

    return result