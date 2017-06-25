# numerical_differentiation.py
"""Volume 1: Numerical Differentiation.
<Name>
<Class>
<Date>
"""

# Problem 1
def fdq1(f, pts, h=1e-5):
    """
    Calculate the first order forward difference quotient.
    Inputs:
        f(function): A callable function.
        pts(NumPy array): An n-dimensional array representing a point in R^n.
        h(float): Defaults to 1e-5.
    Returns:
        (NumPy array): An array of approximations.
    """
    raise ValueError("Problem 1 forward not implemented")

def bdq2(f, pts, h=1e-5):
    """
    Calculate the second order backward difference quotient.
    Inputs:
        f(function): A callable function.
        pts(NumPy array): An n-dimensional array representing a point in R^n.
        h(float): Defaults to 1e-5.
    Returns:
        (NumPy array): An array of approximations.
    """
    raise ValueError("Problem 1 backward not implemented")

def cdq2(f, pts, h=1e-5):
    """
    Calculate the second order centered difference quotient.
    Inputs:
        f(function): A callable function.
        pts(NumPy array): An n-dimensional array representing a point in R^n.
        h(float): Defaults to 1e-5.
    Returns:
        (NumPy array): An array of approximations.
    """
    raise ValueError("Problem 1 second order centered not implemented")

def cdq4(f, pts, h=1e-5):
    """
    Calculate the fourth order centered difference quotient.
    Inputs:
        f(function): A callable function.
        pts(NumPy array): An n-dimensional array representing a point in R^n.
        h(float): Defaults to 1e-5.
    Returns:
        (NumPy array): An array of approximations.
    """
    raise ValueError("Problem 1 fourth order centered not implemented")

# Problem 2
def error_plot(pt):
    """
    Calculate and plot the errors for the following:
        1. Second order backward difference quotient.
        2. Second order centered difference quotient.
        3. Fourth order centered difference quotient.
    Do this for at least 6 values of h in the range [1e-8, 1]
    and for the function f(x)=(sin(x)+1)**x. Use a loglog plot, include a legend
    and mark the values of h on your graph by putting a dot there.
    Inputs:
        pt(float): Point where the derivative is being approximated at.
    """
    raise ValueError("Problem 2 not implemented")

# Problem 3
def prob3(filename="plane.txt"):
    """
    Return the velocity of the plane, which is the derivative of the position.
    Use the radar dish angles to dertmine the position of the plane at discrete
    points. Then use these points to approximate the derivative using difference
    quotients. Use centered difference quotients for the interior points and
    forward/backward for the two endpoints. Plot the trajectory and
    velocities on seperate graphs.
    Hint: NumPy trig functions only accept radians
    Input:
        filename(string): The name of the file that has the data for t, alpha,
            & beta.
    Returns:
        (array): An array of floats containing the approximate velocity at each
            point.
    """
    raise ValueError("Problem 3 not implemented")

# Problem 4
def jacobian(f, n, m, pt, h=1e-5):
    """
    Compute the approximate Jacobian matrix of f at pt using the centered
        difference quotient.
    Inputs:
        f (function): the multidimensional function for which the derivative
            will be approximated.
        n (int): dimension of the domain of f.
        m (int): dimension of the range of f.
        pt (NumPy array): an n-dimensional NumPy array representing a point in R^n.
        h (float): a float to use in the centered difference approximation.
    Returns:
        (ndarray) the mxn Jacobian matrix of f at pt using the centered difference
            quotient.
    """
    raise ValueError("Problem 4 not implemented")

# Problem 5
def findError():
    """
    Compute the maximum error of jacobian() for the function
        f(x,y)=[(e^x)sin(y) + y^3, 3y - cos(x)] on the square [-1,1]x[-1,1].
    Returns:
        (float) Maximum error of your jacobian function.
    """
    raise ValueError("Problem 5 not implemented")
