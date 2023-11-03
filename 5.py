# First, we need to import the necessary libraries for 3D plotting
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the surface
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z1 = np.sqrt(4 - X**2)
Z2 = -np.sqrt(4 - X**2)

# Define the line
t = np.linspace(-1, 1, 100)
LX = 5 - 5*t
LY = 3*t
LZ = 4*t

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100)
ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100)

# Plot the line
ax.plot(LX, LY, LZ, label='Line: (5 - 5t, 3t, 4t)', color='b')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the legend
ax.legend()

# Show the plot
plt.show()
