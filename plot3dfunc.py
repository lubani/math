import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_function(ax, func, title, xlim=(-2, 2), ylim=(-2, 2), zlim=(-2, 2), resolution=100):
    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax.set_title(title)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_zlim(zlim)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

def saddle_point(x, y):
    return x**2 - y**2

def cylinder(x, y):
    r = 1  # Radius of the cylinder
    z = np.sqrt(np.clip(r**2 - x**2, 0, None))
    return z

def sphere(x, y):
    R = 1  # Radius of the sphere
    z = np.sqrt(np.clip(R**2 - x**2 - y**2, 0, None))
    return z

def main():
    fig = plt.figure(figsize=(15, 5))

    ax1 = fig.add_subplot(131, projection='3d')
    plot_3d_function(ax1, saddle_point, 'Saddle Point', zlim=(-2, 2))

    ax2 = fig.add_subplot(132, projection='3d')
    plot_3d_function(ax2, cylinder, 'Cylinder', zlim=(0, 1))

    ax3 = fig.add_subplot(133, projection='3d')
    plot_3d_function(ax3, sphere, 'Sphere', zlim=(0, 1))

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
