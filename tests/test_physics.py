from orbitlab.physics import escape_velocity
from orbitlab.units import ureg


def test_escape_velocity():
    earth_mass = 5.972e24 * ureg.kg
    earth_radius = 6371e3 * ureg.meter

    v = escape_velocity(earth_mass, earth_radius)

    assert v.magnitude > 10000
