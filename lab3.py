import matplotlib.pyplot as plt
import numpy as np

def plot_half_sphere(radius, center, num_points=6):
    phi = np.linspace(0, np.pi / 2, num_points)
    theta = np.linspace(0, 2 * np.pi, num_points)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.sin(phi) * np.cos(theta) + center[0]
    y = radius * np.sin(phi) * np.sin(theta) + center[1]
    z = radius * np.cos(phi) + center[2]
    return x, y, z

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = 0.5
b = 2 * a
c = a

radius = np.sqrt((2 * a)**2 + (2 * b)**2) / 2
center = np.array([0, 0, 0])

x, y, z = plot_half_sphere(radius, center)
ax.plot_surface(x, y, z, color='blue', alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Half sphere and wedge')
plt.show()
