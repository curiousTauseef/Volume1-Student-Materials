# differentiation.py
"""Volume 1: Differentiation.
<Name>
<Class>
<Date>
"""

#Problem 1
def prob1():
    """Return the derivative of e^sin(cos(x)) at x=1 as a float using SymPy."""
    raise ValueError("Problem 1 Not Implemented.")

# Problem 2
def fdq1(f, pts, h=1e-5):
    """Calculate the first order forward difference quotient."""
    raise ValueError("Forward Quotient Not Implemented")

def bdq2(f, pts, h=1e-5):
    """Calculate the second order backward difference quotient."""
    raise ValueError("Backward Quotient Not Implemented.")

def cdq2(f, pts, h=1e-5):
    """Calculate the second order centered difference quotient."""
    raise ValueError("2nd Order Center Quotient Not Implemented.")

def cdq4(f, pts, h=1e-5):
    """Calculate the fourth order centered difference quotient."""
    raise ValueError("4th Order Center Quotient Not Implemented.")

# Problem 3
def error_plot(pt):
    """
    For the function f(x)=(sin(x)+1)**x, calculate and plot the errors for
    the following:
        1. Second order backward difference quotient
        2. Second order centered difference quotient
        3. Fourth order centered difference quotient
    Do this for at least 6 evenly-spaced values of h in the range [1e-8, 1].
    Use a loglog plot, include a legend and mark the values of h on your graph
    by putting a noticeable dot there.

    Parameters:
        pt(float): Point where the derivative is being approximated at.
    """
    raise ValueError("Problem 3 Not Implemented.")

# Problem 4
def prob4(filename="plane.txt"):
    """
    Return the speed of the plane, which is the derivative of the position.
    Use the radar dish angles to determine the position of the plane at discrete
    points. Then use these points to approximate the derivative using difference
    quotients. Use centered difference quotients for the interior points and
    forward/backward for the two endpoints. Plot the trajectory and
    speeds on seperate graphs.

    Parameters:
        filename(string, optional): The name of the file that has the data for
            t, alpha, and beta. Defaults to "plane.txt".
    Returns:
        (array): An array of floats containing the approximate speed at each
            point.
    """
    raise ValueError("Problem 4 Not Implemented.")

# Problem 5
def center_jac(f, n, m, pt, h=1e-5):
    """
    Compute the approximate Jacobian matrix of f at pt using the second order
    centered difference quotient.

    Parameters:
        f (function): the multidimensional function for which the derivative
            will be approximated.
        n (int): dimension of the domain of f.
        m (int): dimension of the range of f.
        pt (NumPy array): an n-dimensional NumPy array representing a point in
            R^n.
        h (float, optional): a float to use in the centered difference
            approximation. Defaults to 10^-5.

    Returns:
        (NumPy array) the (m x n)-dimensional Jacobian matrix of f at pt using
            the second order centered difference quotient.
    """
    raise ValueError("Problem 5 Not Implemented.")

# Problem 6
def prob6():
    """Compute the derivative of ln(sqrt(sin(sqrt(x)))) at x = pi/4 using SymPy,
    the second order centered difference quotient and autograd. Print the
    computation time and error for each method. Return the value of the
    autograd approximation.

    Returns:
        (float): Value of the derivative approximated by autograd.
    """
    raise ValueError("Problem 6 Not Implemented.")

# Problem 7
def prob7():
    """
    Use autograd to take the first and second derivatives of the Taylor series
    of sin(x). Plot the original function along with its two derivatives on the
    interval [-pi,pi].
    """
    raise ValueError("Problem 7 Not Implemented.")

# Problem 8
def prob8():
    """
    Compute the Jacobian for the function
    f(x,y) = [(e^x)sin(y) + y^3, 3y - cos(x)] using Sympy, the second order
    centered difference quotient and autograd. Print the computation time for
    each differentiation technique. Return the value of the autograd
    approximation.

    Returns:
        (array): The value of the jacobian found using autograd at (1,1).
    """
    raise ValueError("Problem 8 Not Implemented.")
