import matplotlib.pyplot as plt


def plot_orbit(x, y, central_body_radius=None):
    """
    Plot a 2D orbital trajectory.

    Parameters
    ----------
    x : array-like
        X positions.

    y : array-like
        Y positions.

    central_body_radius : float, optional
        Radius of the central body for visualization.
    """

    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot trajectory
    ax.plot(x, y, label="Orbit")

    # Plot central body
    ax.scatter(0, 0, s=200, label="Central Body")

    # Optional central body circle
    if central_body_radius is not None:
        circle = plt.Circle(
            (0, 0),
            central_body_radius,
            fill=False,
        )
        ax.add_patch(circle)

    ax.set_xlabel("x position (m)")
    ax.set_ylabel("y position (m)")

    ax.set_title("Orbital Trajectory")

    ax.axis("equal")

    ax.grid(True)

    ax.legend()

    plt.show()
