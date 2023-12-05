import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = 1.0
b = 1.5 * a
c = 12 * a
A = np.array([-b, -a, 0])
B = np.array([-b, a, 0])
C = np.array([b, a, 0])
D = np.array([b, -a, 0])

E = np.array([-b, 0, c])
F = np.array([b, 0, c])

#                 0  1  2  3  4  5
verts = np.array([A, B, C, D, E, F])

faces: list = [
    [0, 1, 2, 3],
    [0, 1, 4],
    [2, 3, 5],
    [0, 4, 5, 3],
    [1, 4, 5, 2]
]

if __name__ == "__main__":
    klin = [Poly3DCollection([verts[face] for face in faces], alpha=0.9, facecolor='brown', edgecolor='k')]
    ax.add_collection3d(klin[0])
    X = 1
    ax.auto_scale_xyz([-2 * X, 2 * X], [-2 * X, 2 * X], [0, 12 * X])
    plt.show()
