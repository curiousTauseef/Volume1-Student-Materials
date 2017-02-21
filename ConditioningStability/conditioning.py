# conditioning.py
"""Volume 1B: Conditioning.
<Name>
<Class>
<Date>
"""

import numpy as np

# Problem 1
def prob1():
    """Randomly perturb w_coeff by replacing each coefficient a_i with
    a_i*r_i, where r_i is drawn from a normal distribution centered at 1 with
    standard deviation 1e-10.

    Plot the roots of 100 such experiments in a single graphic, along with the
    roots of the unperturbed polynomial w(x).

    Using the final experiment only, estimate the relative and absolute
    condition number (in any norm you prefer).

    Returns:
        Display a graph of all 100 perturbations.
        Print the values of relative and absolute condition numbers.
    """
    w_roots = np.arange(1, 21)
    w_coeffs = np.array([1, -210, 20615, -1256850, 53327946, -1672280820,
                        40171771630, -756111184500, 11310276995381,
                        -135585182899530, 1307535010540395,
                        -10142299865511450, 63030812099294896,
                        -311333643161390640, 1206647803780373360,
                        -3599979517947607200, 8037811822645051776,
                        -12870931245150988800, 13803759753640704000,
                        -8752948036761600000, 2432902008176640000])
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def eig_condit(M):
    """Approximate the condition number of the eigenvalue problem at M.

    Inputs:
        M ((n,n) ndarray): A square matrix.

    Returns:
        (float) absolute condition number of the eigenvalue problem at M.
        (float) relative condition number of the eigenvalue problem at M.
    """
    raise NotImplementedError("Problem 2 Incomplete")

def plot_eig_condit(x0=-100, x1=100, y0=-100, y1=100, res=10):
    """Create a grid [x0, x1] x [y0, y1] with the given resolution. For each
    entry (x,y) in the grid, find the relative condition number of the
    eigenvalue problem, using the matrix   [[1 x]
                                            [y 1]]  as the input.
    Use plt.pcolormesh() to plot the condition number over the entire grid.

    Inputs:
        x0 (float): min x-value.
        x1 (float): max x-value.
        y0 (float): min y-value.
        y1 (float): max y-value.
        res (int): number of points along each edge of the grid.
    """
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def integral(n):
    """Calculate the integral from 0 to 1 of x^n e^{x-1} dx using the closed
    form solution (-1)^n !n + (-1)^{n+1} n!/e.
    """
    raise NotImplementedError("Problem 3 Incomplete")

def prob3():
    """For the values of n in the problem, compute integral(n). Compare
    the values to the actual values, and print your explanation of what
    is happening.
    """
    # Actual values of the integral at specified n.
    actual_values = {    1: 0.367879441171,   5: 0.145532940573,
                        10: 0.0838770701034, 15: 0.0590175408793,
                        20: 0.0455448840758, 25: 0.0370862144237,
                        30: 0.0312796739322, 35: 0.0270462894091,
                        40: 0.023822728669,  45: 0.0212860390856,
                        50: 0.0192377544343                         }
    raise NotImplementedError("Problem 3 Incomplete")
