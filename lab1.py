import numpy as np
import matplotlib.pyplot as plt

a = -5

phi = np.linspace(0, 2*np.pi, int(2e5))
r = np.sqrt(a**2 * np.cos(2*phi))
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.plot(phi, r)
ax.set_title("Polar graph of ρ**2=a**2 * cos2ϕ")
plt.show()