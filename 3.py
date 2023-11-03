import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fractions import Fraction


# Create a function to format a number as a fraction
def format_fraction(number, tolerance=1e-10):
    return str(Fraction(number).limit_denominator(int(1 / tolerance)))


if __name__ == "__main__":
    # Define the plane
    A, B, C, D = 2, -1, 1, 12
    # Define the normal vector of the plane
    n = np.array([A, B, C])

    # Define a point in the plane
    p0 = np.array([0, 0, D])

    # Define the point
    p = np.array([2, -3, 3])

    # Calculate the vector from p0 to p
    r = p - p0

    # Calculate the dot product of r and n
    dot_product = np.dot(r, n)

    # Calculate the magnitude of the normal vector
    norm_n = np.linalg.norm(n)

    # Calculate the projection
    projection = p - (dot_product / norm_n ** 2) * n
    print("projection = ", projection)

    # Calculate the distance
    numerator = abs(A * p[0] + B * p[1] + C * p[2] - D)
    denominator = np.sqrt(A ** 2 + B ** 2 + C ** 2)
    distance = numerator / denominator

    print("Distance between the point and the plane: ", distance)

    # Create the figure
    fig = plt.figure()

    # Add 3d axes
    ax = fig.add_subplot(111, projection='3d')

    # Plot the plane
    xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
    zz = (12 - 2 * xx + yy) / 1.0
    ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100)

    # Plot the point
    ax.scatter(*p, color='r', s=100)
    ax.text(*p, f"Point {tuple(p)}")

    # Plot the projection
    ax.scatter(*projection, color='b', s=100)
    projection_fraction = [format_fraction(coord) for coord in projection]
    ax.text(*projection, f"Projection {tuple(projection_fraction)}")

    # Plot the line
    ax.plot(*zip(p, projection), color='k', linestyle='dotted')

    # Set the limits
    ax.set_xlim([0, 5])
    ax.set_ylim([-5, 0])
    ax.set_zlim([0, 5])

    plt.show()
