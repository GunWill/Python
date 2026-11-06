import numpy as np
import matplotlib.pyplot as plt

def analyze_error(solution, f, method, *args, plot_error = False, plot_converge = False):
    #Analyze error of an iterative method with a known solution
    iterations = []
    for i in method(*args): #Loop through every value given by the given method
        iterations.append(i) #append each to the list
    if len(iterations)< 2:
        raise RuntimeError("Numerical method didn't produce enough iterations")

    errors = [abs(x-solution) for x in iterations] #absolute error at every iteration
    n_check = min(5, len(errors)) #Check last 5 errors for divergence
    tail_errors = errors[-n_check:] #Extract tail of error list
    if all(tail_errors[i] < tail_errors[i + 1] for i in range(len(tail_errors) - 1)): #If error in the tail is greater than / equal to previous
        raise RuntimeError(f"Numerical method diverged. Last errors: {tail_errors}") #Raise error and print errors

    if plot_error:
        rel_errors = [] #Stores percent relative errors
        for i in range(1, len(iterations)): #Loop through iterations, starting at second
            x2 = iterations[i] #Find current iteration
            x_prev = iterations[i - 1]

            if x2 != 0:
                rel_err = abs((x2 - x_prev) / x2) * 100 #Calculate relative error given x2 is not 0
            else:
                rel_err = abs((x2-x_prev) * 100) #Given x2 is 0
            rel_errors.append(rel_err)

        iters_err = np.arange(1, len(rel_errors) + 1) #Create array of iteration number beginning at 1

        #plotting:
        plt.figure()
        plt.semilogy(iters_err, rel_errors, 'bo-')
        plt.xlabel('Iteration')
        plt.ylabel('Percent Relative Error')
        plt.title('Relative Error vs Iteration #')
        plt.grid(True, which= 'both')
        plt.tight_layout()
        plt.show()

    if plot_converge:
        x_prev = np.array(iterations[:-1]) #Creates array of all iterations but last one
        x_curr = np.array(iterations[1:]) #Create array of all but first

        plt.figure()
        plt.plot(x_prev, x_curr, 'ro-')
        plt.xlabel('Previous iteration')
        plt.ylabel('Current iteration')
        plt.title('Convergence Plot')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    #Estimating order of convergence - finding slope of log-converted errors

    # n_skip = min(3, len(errors) -2)
    # errors_to_use = errors[:n_skip if n_skip > 0 else errors]

    # log_errors = [] #Create list to store log-transformed errors
    # for e in errors_to_use:
    #     if e > 0:
    #         log_errors.append(np.log(e))
    #     else:
    #         log_errors.append(np.log(np.finfo(float).tiny)) #If e is 0, use log of machine epsilon (smallest possible floating point num), as log(0) is undefined

    # log_errors = np.array(log_errors) #Convert list to numpy array
    # x_fit = log_errors[:-1] 
    # y_fit = log_errors[1:]

    # filter = np.isfinite(x_fit) & np.isfinite(y_fit) #filters out inf or nan values
    # x_fit = x_fit[filter]
    # y_fit = y_fit[filter]
    # if len(x_fit) < 2:
    #     raise RuntimeError("Not enough error values to estimate order")

    # coeffs = np.polyfit(x_fit, y_fit, 1) #Use polyfit to perform linear regression
    # slope = coeffs[0]
    # return float(slope) #Estimated order of convergence


    #Computing percentage relative errors for each equation, previous code did not work for NR or secant as they converged too fast
    rel_errors = []
    for i in range(1, len(iterations)):
        x_i = iterations[i] #current iteration
        x_prev = iterations[i - 1] #Previous iteration
        if x_i != 0:
            rel_err = abs((x_i - x_prev) / x_i) * 100
        else:
            rel_err = abs(x_i - x_prev) * 100 #Handle division of 0
        rel_errors.append(rel_err)

    # Convert to log scale, keeping only positive values
    log_rel_errors = [np.log(r) for r in rel_errors if r > 0]

    if len(log_rel_errors) < 2:
        raise RuntimeError("Not enough relative error values to estimate order") #Need at least two pionts to fit a line

    x_fit = np.array(log_rel_errors[:-1]) #Slope of this line gives convergence
    y_fit = np.array(log_rel_errors[1:])

    if len(x_fit) < 2:
        raise RuntimeError("Not enough error values to estimate order")

    coeffs = np.polyfit(x_fit, y_fit, 1) #Handles linear regression
    slope = coeffs[0]
    return float(slope) #Estimated order of convergence

    


def bisection(f, a, b, tol = 1e-6, max_iter = 100): #bisection method for checks -> same as HW1
    fa = f(a) #Function at left endpoint
    fb = f(b) #Function at right endpoint

    if fa*fb > 0:
        raise ValueError("No root between f(a) and f(b)")

    for i in range(max_iter):
        c = (a + b) / 2.0
        yield c #Yield the midpoint as current estimate
        fc = f(c)
        if abs(fc) < tol or (b-a) / 2.0 < tol:
            break
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

def NR(f, df, x0, tol = 1e-6, max_iter = 100): #Newton Raphson method for checks -> HW1
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivative is 0")
        x_new = x-fx / dfx #NR part
        yield x_new
        if abs(x_new - x) < tol:
            break
        x = x_new

def fixed_point(g, x0, tol = 1e-6, max_iter = 100): #Fixed oint method for checks -> HW1
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        yield x_new
        if abs(x_new - x) < tol:
            break
        x = x_new

def secant(f, x0, x1, tol = 1e-6, max_iter = 100): #Secant method for checks -> HW1
    for i in range(max_iter - 1):
        f0 = f(x0)
        f1 = f(x1)
        if f1 - f0 ==0:
            raise ZeroDivisionError("Denom is zero")
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        yield x2
        if abs(x2 - x1) < tol:
            break
        x0 = x1
        x1 = x2

def test(): #Runs test cases
    print("Testing...")
    print("Bisection:")
    def f1(x):
        return x**2 - 2
    #Estimates order of convergence & pulls up plots
    order1 = analyze_error(solution = np.sqrt(2.0), f = f1, 
                           method = lambda: bisection(f1, 0.0, 3.0, tol = 1e-10, max_iter = 100),#lambda wraps method call so analyze_error can invoke 
                           plot_error = True, plot_converge = True)
    print(f"Estimated order of convergence: {order1:.4f}")

    print("Newton Raphson...")
    def df1(x):
        return 2 * x
    #Same as above but for NR
    order2 = analyze_error(solution = np.sqrt(2.0), f=f1,
                            method = lambda: NR(f1, df1, x0=1.5, tol = 1e-10, max_iter = 100),
                            plot_error = True, plot_converge = True)
    print(f"Estimated order of convergence: {order2:.4f}")

    print("Fixed Point...")
    def g(x):
        return np.cos(x)

    def f3(x):
        return x - np.cos(x)

    #True solution is where cos(x) = x -> As found in f3
    order3 = analyze_error(solution = 0.7390851332151, f=f3,
                           method = lambda: fixed_point(g, x0 = 0.5, tol = 1e-10, max_iter = 100),
                           plot_error = True, plot_converge=True)
    print(f"Estimated order of convergence: {order3:.4f}")

    print("Secant...")

    def f4(x):
        return x ** 3 - 2 * x - 5
    #Where f4 = 0, root of f4
    order4 = analyze_error(solution = 2.0945514815423, f = f4,
                           method = lambda: secant(f4, x0=2.0, x1=2.1, tol = 1e-10, max_iter = 100),
                           plot_error = True, plot_converge = True)
    print(f"Estimated order of convergence: {order4:.4f}")

    print("All tests complete")

if __name__ == "__main__":
    test()