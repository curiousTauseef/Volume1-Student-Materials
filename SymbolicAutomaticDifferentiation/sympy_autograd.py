# sympy_autograd.py
"""Volume 1: Symbolic and Automatic Differentiation.
<Name>
<Class>
<Date>
"""
import sympy as sy
import numpy as np
import autograd.numpy as anp

# Problem 1
def prob1():
	""" Write out the expression 2/5*e^(x^2-y)cosh(x+y) + 3/7*log(xy+1) in SymPy.
	
	Returns:
	 The SymPy Expression 
	"""
	raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def prob2():
    """Solve y = sqrt(5-e^x^2) for x.
    
    Returns:
        (list): The list of expressions that solves for x.
    """
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3():
    """Calculate the derivative of e^sin(cos(x)) at x = 1.
    Time how long it takes to compute the derivative using SymPy.
    Time the same derivative using the second order centered difference quotient.
	Calculate the error for each approximation.

    Print the time it takes to compute and the error for both SymPy and
    centered difference quotients.

    Returns:
        (float): SymPy approximation of e^sin(cos(x)) at x = 1.
    """

    raise NotImplementedError("Problem 3 Incomplete")

#Problem 4
def prob4():
	"""Evaluate the 3rd derivative of tanh(x) at 10,000 randomly generated points
	using .subs() method and the lambdify() function. 
	
	Print the time it takes to compute the 3rd derivative of tanh(x) of these 
	two methods. 
	"""
	raise NotImplementedError("Problem 3 Incomplete")


# Problem 5
def prob5():
    """Compute the derivative of ln(sqrt(sin(sqrt(x)))) at x = pi/4.
    Times how long it take to compute using SymPy, Autograd, and centered
    difference quotients. Compute the error of each approximation.

    Print the time and error for each computation. 
    
    """
    raise NotImplementedError("Problem 5 Incomplete")

# Problem 6
def prob6():
	""" Use elementwise_grad() from autograd to create the following functions: f(x) = 1/cosh(x) 
	and its next 5 derivatives df(x),d2f(x),d3f(x),d4f(x), and d5f(x) from [-7,7]. 
		
	Plot each function in multiple subplots.
	
	"""
	raise NotImplementedError("Problem 6 Incomplete")

# Problem 7
def prob7():
    """Compute Jacobian for the function
        f(x,y)=[(e^x)sin(y) + y^3, 3y - cos(x)]
    Time how long it takes to compute the Jacobian using SymPy and autograd.

    Print the computation times.

    Returns:
        Jacobian (array): jacobian found using Autograd at (1,1).
    """
    
    raise NotImplementedError("Problem 7 Incomplete")
