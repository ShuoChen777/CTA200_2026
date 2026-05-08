"""
Some functions needed for question 2 of assignment 3
"""

def get_derivatives(t, Y, s=10, r=28, b=8/3):
    """
    Gets the derivative values for x, y and z by the simultaneous differential equations:

    dx = -s(x - y)
    dy = rx - y - xz
    dz = -bz + xy

    Parameters
    ----------
    t: float
        arbitrary time value
    Y: tuple
        the amplitude of the x, y and z - directions. In the form (x, y, z)
    s: float (optional)
        sigma, the Prandtl number
    r: float (optional)
        Rayleigh number
    b: float (optional)
        dimensionless length scale

    Returns
    -------
    (dx, dy, dz): tuple
        derivatives of amplitude in each direction
    """
    x, y, z = Y[0], Y[1], Y[2]
    dx = -s * (x - y)
    dy = (r * x) - y - (x * z)
    dz = (-b * z) + (x * y)

    return (dx, dy, dz)