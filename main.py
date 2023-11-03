import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def plot_pyramid_and_calculate_volume(A, B, C, D):
    # Create the vectors AB, AC and AD
    AB = np.subtract(B, A)
    AC = np.subtract(C, A)
    AD = np.subtract(D, A)
    cross_prod = np.cross(AB, AC)
    # Calculate the area of the triangle
    area = 0.5 * np.linalg.norm(cross_prod)
    print("area is ", area)
    # Calculate the volume of the pyramid
    volume = abs(np.dot(AD, cross_prod) / 6.0)
    # Prepare the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the points
    ax.scatter(*zip(A, B, C, D), color='b')

    # Place the coordinates next to the dots
    for point, name in zip([A, B, C, D], ["A", "B", "C", "D"]):
        ax.text(*point, f"{name}{tuple(point)}")

    # Plot the triangular pyramid
    vertices = np.array([A, B, C, D])
    triangles = [[vertices[0], vertices[1], vertices[2]],
                 [vertices[0], vertices[1], vertices[3]],
                 [vertices[0], vertices[2], vertices[3]],
                 [vertices[1], vertices[2], vertices[3]]]

    face_collection = Poly3DCollection(triangles, linewidths=1, edgecolors='r', alpha=.25)
    ax.add_collection3d(face_collection)

    # Setting the axes properties
    ax.set_xlim3d(min(A[0], B[0], C[0], D[0]), max(A[0], B[0], C[0], D[0]))
    ax.set_ylim3d(min(A[1], B[1], C[1], D[1]), max(A[1], B[1], C[1], D[1]))
    ax.set_zlim3d(min(A[2], B[2], C[2], D[2]), max(A[2], B[2], C[2], D[2]))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    return volume

# Usage
if __name__ == "__main__":

    A = np.array([-2, -1, -4])
    B = np.array([-3, -3, 4])
    C = np.array([2, 2, -3])
    D = np.array([-2, 3, -1])

    print("Volume of the pyramid: ", plot_pyramid_and_calculate_volume(A, B, C, D))
    plt.show()

    n = np.array([2, -1, 1])
    v = np.array([-4, -3, 3])

    # Projection
    proj_n_v = (np.dot(v, n) / np.linalg.norm(n) ** 2) * n

    # Distance
    distance = np.linalg.norm(proj_n_v)

    print("Projection vector: ", proj_n_v)
    print("Distance: ", distance)

