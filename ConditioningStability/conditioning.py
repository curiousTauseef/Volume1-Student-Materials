# conditioning.py
"""Volume 1: Conditioning.
<Name>
<Class>
<Date>
"""

import numpy as np


# Problem 1
def prob1(A):
    """Calculate the condition number of a matrix using the 2-norm for matrices.
    
    Parameters:
        A ((m,n) ndarray): A matrix.
    
    Returns:
        x (float): The condition number of the matrix.
    """
    raise NotImplementedError("prob1 incomplete")

    
# Problem 2
def prob2():
    """Randomly perturb w_coeff by replacing each coefficient a_i with
    a_i*r_i, where r_i is drawn from a normal distribution centered at 1 with
    standard deviation 1e-10.

    Plot the roots of 100 such experiments in a single graphic, along with the
    roots of the unperturbed polynomial w(x).

    Using the final experiment only, using the infinity norm, estimate the
    relative and absolute condition number.

    Returns:
        Display a graph of all 100 perturbations.
        tuple (float): A tuple containing the average absolute and relative 
            condition numbers
    """
    raise NotImplementedError("prob2 incomplete")


# Problem 3
def eig_condit(M):
    """Approximate the condition number of the eigenvalue problem at M.

    Parameters:
        M ((n,n) ndarray): A square matrix.

    Returns:
        (float) absolute condition number of the eigenvalue problem at M.
        (float) relative condition number of the eigenvalue problem at M.
    """
    raise NotImplementedError("eig_condit incomplete")

# Problem 4
def prob4(x0=-100, x1=100, y0=-100, y1=100, res=10):
    """Create a grid [x0, x1] x [y0, y1] with the given resolution. For each
    entry (x,y) in the grid, find the relative condition number of the
    eigenvalue problem, using the matrix   [[1, x], [y, 1]]  as the input.
    Use plt.pcolormesh() to plot the condition number over the entire grid.

    Parameters:
        x0 (float): min x-value.
        x1 (float): max x-value.
        y0 (float): min y-value.
        y1 (float): max y-value.
        res (int): number of points along each edge of the grid.
    """
    raise NotImplementedError("prob4 incomplete")
    
    
# Problem 5
def lstsq_normal(A, b):
    """Calculate the least squares solution of Ax=b directly using the normal
    equation
    
    Inputs:
        A ((m,n), ndarray): A matrix of size m>=n
        b ((m, ), ndarray): A vector of length m
        
    Returns:
        x ((m, ), ndarray): The vector solution to the normal equation
    """
    raise NotImplementedError("lstsq_normal incomplete")
    
    
def lstsq_qr(A, b):
    """Calculate the least squares solution of Ax=b using the QR decomposition.
    
    Inputs:
        A ((m,n), ndarray): A matrix of size m>=n
        b ((m, ), ndarray): A vector of length m
        
    Returns:
        x ((m, ), ndarray): The vector solution to the normal equation
    """
    raise NotImplementedError("lstsq_qr incomplete")
    
    
def prob5():
    """Approximate e^sin(4x) on the interval [0,1] with a 14 degree polynomial using
    the least squares method. Solve the least squares problem using the the normal 
    equation and the QR decomposition and then compare the solutions by plotting
    them together with the interpolated function.  Return the mean squared error of
    both solutions, ||Ax-b||_2.
    
    Returns:
        error1 (float): The mean squared error of the direct approach
        error2 (float): The mean squared error using the QR decomposition
    """
    raise NotImplementedError("prob5 incomplete")