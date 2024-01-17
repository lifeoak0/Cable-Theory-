import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
dx = 0.05  # space step (increased for stability)
dt = 0.001  # time step (decreased for stability)
t_max = 10
x_max = 1
D = 1  # diffusion coefficient

# Stability check for the finite difference method
if D * dt / dx**2 > 0.5:
    raise ValueError("The simulation might be unstable. Decrease dt or increase dx.")

# Initialization
x_steps = int(x_max / dx)
t_steps = int(t_max / dt)
u = np.zeros((t_steps, x_steps))  # potential u at time t and position x

# Initial condition (e.g., a peak in the middle of the cable)
u[0, x_steps//2] = 1

# Boundary conditions (e.g., u = 0 at both ends)
u[:, 0] = 0
u[:, -1] = 0

# Finite difference method
for t in range(0, t_steps - 1):
    for x in range(1, x_steps - 1):
        u[t + 1, x] = u[t, x] + (D * dt / dx**2) * (u[t, x+1] - 2*u[t, x] + u[t, x-1])

# Visualization
X, T = np.meshgrid(np.linspace(0, x_max, x_steps), np.linspace(0, t_max, t_steps))
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u, cmap='viridis')
ax.set_xlabel('Space')
ax.set_ylabel('Time')
ax.set_zlabel('Potential')
ax.set_title('Cable Theory Model - Optimized')
plt.show()
