import numpy as np
from orbitlab.physics import orbital_velocity
from orbitlab.simulation import simulate_orbit
from orbitlab.units import ureg


def test_simulation_runs():
    """
    Ensure orbit simulation executes successfully.
    """

    earth_mass = 5.972e24 * ureg.kg

    radius = 7000e3 * ureg.meter

    velocity = orbital_velocity(earth_mass, radius)

    initial_position = np.array([radius.magnitude, 0]) * ureg.meter

    initial_velocity = np.array([0, velocity.magnitude]) * (ureg.meter / ureg.second)

    steps = 1000

    x, y = simulate_orbit(
        earth_mass,
        initial_position,
        initial_velocity,
        10 * ureg.second,
        steps,
    )

    # Correct output size
    assert len(x) == steps
    assert len(y) == steps

    # No NaN values
    assert not np.isnan(x).any()
    assert not np.isnan(y).any()

    # Orbit should evolve
    assert x[0] != x[-1]
    assert y[0] != y[-1]
