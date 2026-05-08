"""
    Here is the function that will iterate for question 1
"""
import numpy

def complex_iterate(x, y, maxiter=30):
    """
    Given a complex number c = x + iy with constrants |x|<2 and |y|<2, will iterate to generate values defined by
        z_(i+1) = (z_i)^2 + c,
    given initial value z0 = 0

    Parameters
    ----------
    c: complex
        Input complex number to plug into equation
    maxiter: int
        Maximum number of iterations

    Returns
    -------
    int
        1 if convergent, 0 if divergent
    """
    c = x + (y * 1j)

    z = 0
    for iter in range(maxiter):
        z = (z ** 2) + c
        if z ** 2 > 8:
            return (iter + 1)
    
    return -1

def check_convergence(z):
    if z == -1:
        return -1
    return 0