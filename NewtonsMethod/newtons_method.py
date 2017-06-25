# solutions.py
"""Volume 1: Newton's Method. Solutions File.
<Name>
<Class>
<Date>
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

# Problem 1
def newtons_method(f, x0, Df, iters=15, tol=1e-5, alpha=1.):
    """Use Newton's method to approximate a zero of a function.

    Inputs:
        f (function): A function handle. Should represent a function
            from R to R.
        x0 (float): Initial guess.
        Df (function): A function handle. Should represent the derivative
             of f.
        iters (int): Maximum number of iterations before the function
            returns. Defaults to 15.
        tol (float): The function returns when the difference between
            successive approximations is less than tol.
        alpha (float): Scalar used for backtracking method. Defaults to 1.

    Returns:
        A tuple (x, converged, numiters) with
            x (float): the approximation for a zero of f.
            converged (bool): a Boolean telling whether Newton's method
                converged.
            num_iters (int): the number of iterations computed.
    """
    raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def prob2():
    """Given P1[(1+r)**N1-1] = P2[1-(1+r)**(-N2)], if N1 = 30, N2 = 20,
    P1 = 2000, and P2 = 8000, use Newton's method to determine r.
    Return r.
    """
    raise NotImplementedError("Problem 2 Incomplete")

# Problem 3
def prob3():
    """Find an alpha < 1 so that running Newtons_method() on f(x) = x**(1/3)
    with x0 = .01 converges. Return the complete results of newtons_method().
    """
    raise NotImplementedError("Problem 3 Incomplete")

# Problem 4
def newtons_vector(f, x0, Df, iters=15, tol=1e-5, alpha=1):
    """Use Newton's method to approximate a zero of a vector valued function from R^2 to R^2.

    Inputs:
        f (function): A function handle.
        x0 (nd array): Initial guess.
        Df (function): A function handle. Should represent the derivative
             of f.
        iters (int): Maximum number of iterations before the function
            returns. Defaults to 15.
        tol (float): The function returns when the difference between
            successive approximations is less than tol.
        alpha (float): Defaults to 1.  Allows backstepping.

    Returns:
        A tuple (x_values, y_values) where x_values and y_values are lists that contain the x and y value from each iteration of Newton's method.
    """
    raise NotImplementedError("Problem 4 Incomplete")

# Problem 4
def prob4():
    """Solve the bioremediation system using Newton's method and Newton's method with
    backtracking.
    """
    raise NotImplementedError("Problem 4 Incomplete")

# Problem 5
def plot_basins(f, Df, roots, xmin, xmax, ymin, ymax, numpoints=1000, iters=15, colormap='brg'):
    """Plot the basins of attraction of f.

    INPUTS:
        f (function): Should represent a function from C to C.
        Df (function): Should be the derivative of f.
        roots (nd array): An array of the zeros of f.
        xmin, xmax, ymin, ymax (float,float,float,float): Scalars that define the domain
            for the plot.
        numpoints (int): A scalar that determines the resolution of the plot. Defaults to 100.
        iters (int): Number of times to iterate Newton's method. Defaults to 15.
        colormap (str): A colormap to use in the plot. Defaults to 'brg'.
    """
    raise NotImplementedError("Problem 5 Incomplete")
