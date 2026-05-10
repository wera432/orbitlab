import numpy as np
from numba import njit
from orbitlab.units import G


@njit
def _simulate_orbit_numba(position, velocity, G_value, M, dt, steps):
    positions = np.zeros((steps, 2))

    for i in range(steps):
        r = np.sqrt(position[0] ** 2 + position[1] ** 2)

        acceleration = -G_value * M * position / r**3

        velocity += acceleration * dt
        position += velocity * dt

        positions[i] = position

    return positions


def simulate_orbit_python(
    position,
    velocity,
    G_value,
    M,
    dt,
    steps,
):
    positions = np.zeros((steps, 2))

    for i in range(steps):
        r = np.sqrt(position[0] ** 2 + position[1] ** 2)

        acceleration = -G_value * M * position / r**3

        velocity += acceleration * dt
        position += velocity * dt

        positions[i] = position

    return positions


def simulate_orbit(
    central_mass,
    initial_position,
    initial_velocity,
    dt,
    steps,
):
    """
    Simulate a 2D orbit using Euler integration.

    Parameters
    ----------
    central_mass : Pint Quantity
        Mass of the central body.

    initial_position : Pint Quantity
        Initial position vector [x, y].

    initial_velocity : Pint Quantity
        Initial velocity vector [vx, vy].

    dt : Pint Quantity
        Time step.

    steps : int
        Number of simulation steps.

    Returns
    -------
    tuple
        Arrays of x and y positions.
    """

    position = initial_position.to("meter").magnitude.astype(float)
    velocity = initial_velocity.to("meter/second").magnitude.astype(float)

    M = central_mass.to("kilogram").magnitude
    dt = dt.to("second").magnitude

    G_value = G.to("meter^3 / kilogram / second^2").magnitude

    positions = _simulate_orbit_numba(position, velocity, G_value, M, dt, steps)

    return positions[:, 0], positions[:, 1]
