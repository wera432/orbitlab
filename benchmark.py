import time
import numpy as np

from orbitlab.simulation import (
    simulate_orbit_python,
    _simulate_orbit_numba,
)
from orbitlab.units import G

# Initial conditions
position = np.array([7000e3, 0.0])

velocity = np.array([0.0, 7500.0])

G_value = G.to("meter^3 / kilogram / second^2").magnitude

M = 5.972e24

dt = 10.0

steps = 200000


# -----------------------------
# Pure Python benchmark
# -----------------------------
start = time.perf_counter()

simulate_orbit_python(
    position.copy(),
    velocity.copy(),
    G_value,
    M,
    dt,
    steps,
)

python_time = time.perf_counter() - start


# -----------------------------
# First Numba call (includes compilation)
# -----------------------------
_simulate_orbit_numba(
    position.copy(),
    velocity.copy(),
    G_value,
    M,
    dt,
    10,
)


# -----------------------------
# Actual Numba benchmark
# -----------------------------
start = time.perf_counter()

_simulate_orbit_numba(
    position.copy(),
    velocity.copy(),
    G_value,
    M,
    dt,
    steps,
)

numba_time = time.perf_counter() - start


print(f"Pure Python: {python_time:.4f} s")
print(f"Numba:       {numba_time:.4f} s")

print(f"Speedup:     {python_time / numba_time:.2f}x")
