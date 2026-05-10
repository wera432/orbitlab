# OrbitLab

OrbitLab is a lightweight scientific Python package for simulating and visualizing orbital motion using Newtonian gravity.

The project demonstrates:

* Unit-safe scientific computing with Pint
* High-performance numerical simulation with Numba
* Automated testing with pytest
* Continuous Integration using GitHub Actions
* Documentation deployment using MkDocs + GitHub Pages

---

# Features

* Gravitational force calculations
* Orbital velocity calculations
* Escape velocity calculations
* 2D orbit simulation
* Numba-accelerated numerical integration
* Orbit trajectory visualization with Matplotlib
* Unit-safe APIs using Pint

---

# Installation

Clone the repository:

```bash
git clone https://github.com/wera432/orbitlab.git
cd orbitlab
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

## Linux / macOS

```bash
source .venv/bin/activate
```

## Windows

```powershell
.venv\Scripts\activate
```

Install the package:

```bash
pip install -e .
```

---

# Example Usage

```python
import numpy as np

from orbitlab.physics import orbital_velocity
from orbitlab.simulation import simulate_orbit
from orbitlab.visualization import plot_orbit
from orbitlab.units import ureg

# Earth parameters
earth_mass = 5.972e24 * ureg.kg
radius = 7000e3 * ureg.meter

# Circular orbit velocity
velocity = orbital_velocity(earth_mass, radius)

# Initial conditions
initial_position = np.array([
    radius.magnitude,
    0,
]) * ureg.meter

initial_velocity = np.array([
    0,
    velocity.magnitude,
]) * (ureg.meter / ureg.second)

# Run simulation
x, y = simulate_orbit(
    earth_mass,
    initial_position,
    initial_velocity,
    10 * ureg.second,
    5000,
)

# Visualize orbit
plot_orbit(x, y)
```

---

# Physics Background

OrbitLab uses Newtonian gravity.

The gravitational force is:

F = G m₁ m₂ / r²

Circular orbital velocity is:

v = sqrt(GM / r)

Escape velocity is:

v = sqrt(2GM / r)

The simulation uses Euler integration to update:

* position
* velocity
* acceleration

through time.

---

# Numba Acceleration

OrbitLab uses Numba JIT compilation to accelerate orbit simulations.

The numerical integration kernel is implemented using:

```python
@njit
```

This significantly improves performance for large simulations.

Example benchmark results:

| Method      | Runtime |
| ----------- | ------- |
| Pure Python | 2.1 s   |
| Numba       | 0.05 s  |

---

# Testing

Run tests using:

```bash
pytest
```

The project includes tests for:

* orbital velocity
* escape velocity
* simulation stability
* output validation

---

# Code Quality

Linting:

```bash
ruff check .
```

Formatting:

```bash
black .
```

---

# Continuous Integration

GitHub Actions automatically:

* installs dependencies
* runs Ruff
* checks Black formatting
* executes pytest

on every push and pull request.

---

# Documentation

Local documentation preview:

```bash
mkdocs serve
```

Build static documentation:

```bash
mkdocs build
```

Deploy documentation:

```bash
mkdocs gh-deploy
```

---

# Technologies Used

* Python
* NumPy
* Pint
* Numba
* Matplotlib
* Pytest
* Ruff
* Black
* MkDocs
* GitHub Actions

---

# Future Improvements

Potential future extensions:

* Velocity Verlet integration
* Multi-body simulations
* 3D orbital mechanics
* Energy conservation analysis
* Interactive visualization
* Parallel Monte Carlo simulations

---

# License

MIT License


