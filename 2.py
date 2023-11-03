import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the point and the normal vector
A = np.array([3, 4, 2])
n = np.array([1, 0, -1])

# Calculate the coefficients of the plane equation
plane_coefficients = np.append(n, -np.dot(A, n))

# Print the equation of the plane
print(f"Plane equation: {plane_coefficients[0]}x + {plane_coefficients[1]}y + {plane_coefficients[2]}z + {plane_coefficients[3]} = 0")

# Prepare the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the point
ax.scatter(*A, color='b')

# Add the coordinates next to the point
ax.text(*A, f"A{tuple(A)}")

# Plot the normal vector
ax.quiver(*A, *n, color='r')

# Plot the plane
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
zz = (-plane_coefficients[0]*xx - plane_coefficients[1]*yy - plane_coefficients[3]) / plane_coefficients[2]
ax.plot_surface(xx, yy, zz, alpha=0.5)

# Setting the axes properties
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
