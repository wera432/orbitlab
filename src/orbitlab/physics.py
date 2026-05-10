import numpy as np
from orbitlab.units import G


def gravitational_force(m1, m2, r):
    """
    Compute gravitational force between two masses.

    Parameters
    ----------
    m1 : Pint Quantity
        Mass of the first object.
    m2 : Pint Quantity
        Mass of the second object.
    r : Pint Quantity
        Distance between the centers of the objects.

    Returns
    -------
    Pint Quantity
        Gravitational force.
    """
    return G * m1 * m2 / r**2


def orbital_velocity(M, r):
    """
    Compute orbital velocity.

    Parameters
    ----------
    M : Pint Quantity
        Central body mass.
    r : Pint Quantity
        Distance from center.

    Returns
    -------
    Pint Quantity
        Orbital velocity.
    """
    return np.sqrt(G * M / r)


def escape_velocity(M, r):
    """
    Compute escape velocity.

    Parameters
    ----------
    M : Pint Quantity
        Central body mass.
    r : Pint Quantity
        Distance from center.

    Returns
    -------
    Pint Quantity
        Escape velocity.
    """
    return np.sqrt(2 * G * M / r)
