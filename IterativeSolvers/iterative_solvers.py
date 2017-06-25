# iterative_solvers.py
"""Volume 1: Iterative Solvers.
<Name>
<Class>
<Date>
"""

# Helper function
def diag_dom(n, num_entries=None):
    """Generates a strictly diagonally dominant (n, n) matrix.
    Parameters:
        n (int): The dimension of the system.
        num_entries (int): The number of nonzero values.
            Defaults to n^(3/2)-n.
    Returns:
        A ((n,n) Numpy array): A (n, n) strictly diagonally dominant matrix.
    """
    if num_entries is None:
        num_entries = int(n**1.5) - n
    A = np.zeros((n,n))
    rows = np.random.choice(np.arange(0,n), size=num_entries)
    cols = np.random.choice(np.arange(0,n), size=num_entries)
    data = np.random.randint(-4, 4, size=num_entries)
    for i in range(num_entries):
        A[rows[i], cols[i]] = data[i]
    for i in range(n):
        A[i,i] = np.sum(np.abs(A[i])) + 1
    return A

# Problems 1 and 2
def jacobi_method(A, b, tol=1e-8, N=100, plot=False):
    """Calculate the solution to the system Ax = b via the Jacobi Method.
    Parameters:
        A ((n, n) NumPy array): A square matrix.
        b ((n, 1) NumPy array): A vector of length n.
        tol (float, opt): The convergence tolerance.
            Defaults to 10^-8.
        N (int, opt): The maximum number of iterations to perform.
            Defaults to 100.
        plot (bool, opt): If True, plot the convergence rate of the algorithm.
            This parameter is for Problem 2.
            Defaults to False.
    Returns:
        x ((n,1) NumPy array): The solution to system Ax = b.
    """
    raise ValueError("Problems 1 and 2 not Implemented.")

# Problem 3
def gauss_seidel(A, b, tol=1e-8, N=100, plot=False):
    """Calculate the solution to the system Ax = b via the Gauss-Seidel Method.
    Parameters:
        A ((n, n) NumPy array): A square matrix.
        b ((n, 1) NumPy array): A vector of length n.
        tol (float, opt): The convergence tolerance.
            Defaults to 10^-8.
        N (int, opt): The maximum number of iterations to perform.
            Defaults to 100.
        plot (bool, opt): If true, plot the convergence rate of the algorithm.
            Defaults to False.
    Returns:
        x ((n, 1) NumPy array): The solution to system Ax = b.
    """
    raise ValueError("Problem 3 not Implemented.")

# Problem 4
def prob4():
    """For a 5000 parameter system, compare the runtimes of the Gauss-Seidel
    method and la.solve(). Print an explanation of why Gauss-Seidel is so much
    faster.
    """
    raise ValueError("Problem 4 not Implemented.")

# Problem 5
def sparse_gauss_seidel(A, b, tol=1e-8, N=100):
    """Calculate the solution to the sparse system Ax = b via the Gauss-Seidel
    Method.
    Parameters:
        A ((n, n) csr_matrix): A (n, n) sparse CSR matrix.
        b ((n, 1) Numpy array): A vector of length n.
        tol (float, opt): The convergence tolerance.
            Defaults to 10^-8.
        N (int, opt): the maximum number of iterations to perform.
            Defaults to 100.
    Returns:
        x ((n, 1) Numpy array): The solution to system Ax = b.
    """
    raise ValueError("Problem 5 not Implemented.")

# Problem 6
def sparse_sor(A, b, omega, tol=1e-8, N=100):
    """Calculate the solution to the system Ax = b via Successive Over-
    Relaxation.
    Parameters:
        A ((n, n) csr_matrix): A (n, n) sparse matrix.
        b ((n, 1) Numpy Array): A vector of length n.
        omega (float in [0,1]): The relaxation factor.
        tol (float, opt): The convergence tolerance.
            Defaults to 10^-8.
        N (int, opt): The maximum number of iterations to perform.
            Defaults to 100.
    Returns:
        x ((n, 1) Numpy array): The solution to system Ax = b.
    """
    raise ValueError("Problem 6 not Implemented.")

# Problem 7
def hot_plate(n):
    """Generate the system Au = b and then solve it using sparse_sor().
    If show has the value of True, vizualize the solution with a heatmap using
    plt.pcolormesh() ("seismic" is a good color map in this case).
    Parameters:
        n (int): Determines the size of A and b. A is (n**2, n**2) and b is
                 (n**2, 1).
        omega(float in [0,1]): The relaxation factor.
        tol(float, opt): The iteration tolerance.
            Defaults to 10^-8.
        N(int, opt): The maximum number of iterations.
            Defaults to 100.
        plot(bool, opt): Determines whether or not the solution is vizualized.
            Defaults to False.
    Returns:
        u(NumPy array): The n^2 x 1 solution vector u to the system Au=b.
    """
    raise ValueError("Problem 7 not Implemented.")
# Problem 8
def compare_omega():
    """Time hot_plate() with omega = 1, 1.05, 1.1, ..., 1.9, 1.95, tol=1e-2,
    and N = 1000 with A and b generated with n = 20. Plot the times as a
    function of omega.
    """
    raise ValueError("Problem 8 not Implemented.")
